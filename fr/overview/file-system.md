```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/file-system.md
```
# Système de fichiers

LittlevGL a un module d'abstraction de système de fichiers qui permet d'attacher tout type de système de fichiers.
Les systèmes de fichiers sont identifiés par une lettre.
Par exemple, si la carte SD est associée à la lettre `'S'`, un fichier peut être localisé par `"S:path/to/file.txt"`.

## Ajouter un pilote

Pour ajouter un pilote, un `lv_fs_drv_t` doit être initialisé comme ceci :
```c
lv_fs_drv_t drv; 
lv_fs_drv_init(&drv);                     /* Initialisation de base */

drv.letter = 'S';                         /* Une lettre majuscule pour identifier le lecteur */
drv.file_size = sizeof(my_file_object);   /* Taille requise pour enregistrer un objet de fichier */
drv.rddir_size = sizeof(my_dir_object);   /* Taille requise pour enregistrer un objet répertoire (utilisé par dir_open/close/read) */ 
drv.ready_cb = my_ready_cb;               /* Fonction de rappel pour indiquer si le lecteur est prêt à être utilisé */
drv.open_cb = my_open_cb;                 /* Fonction de rappel pour ouvrir un fichier */
drv.close_cb = my_close_cb;               /* Fonction de rappel pour fermer un fichier */
drv.read_cb = my_read_cb;                 /* Fonction de rappel pour lire un fichier */
drv.write_cb = my_write_cb;               /* Fonction de rappel pour écrire un fichier */
drv.seek_cb = my_seek_cb;                 /* Fonction de rappel pour se déplacer dans un fichier (déplacer le curseur) */
drv.tell_cb = my_tell_cb;                 /* Fonction de rappel pour donner la position du curseur */
drv.trunc_cb = my_trunc_cb;               /* Fonction de rappel pour supprimer un fichier */
drv.size_cb = my_size_cb;                 /* Fonction de rappel pour donner la taille d'un fichier */
drv.rename_cb = my_size_cb;               /* Fonction de rappel pour renommer un fichier */


drv.dir_open_cb = my_dir_open_cb;         /* Fonction de rappel pour ouvrir un répertoire et lire son contenu */
drv.dir_read_cb = my_dir_read_cb;         /* Fonction de rappel pour lire le contenu d'un répertoire */
drv.dir_close_cb = my_dir_close_cb;       /* Fonction de rappel pour fermer un répertoire */

drv.free_space_cb = my_size_cb;           /* Fonction de rappel pour donner l'espace libre d'un lecteur */

drv.user_data = my_user_data;             /* Toute donnée personnalisée si nécessaire */

lv_fs_drv_register(&drv);                 /* Finalement enregistre le lecteur */

```

N'importe laquelle des fonctions de rappel peut être `NULL` pour indiquer que l'opération n'est pas prise en charge.

Si vous utilisez `lv_fs_open(&file, "S:/folder/file.txt",  LV_FS_MODE_WR)` LittlevGL effectue les opérations suivantes
1. vérifie s'il y a un lecteur avec la lettre `'S'`
2. vérifie si `open_cb` est implémentée (pas `NULL`)
3. appelle `open_cb` avec le chemin `"folder/file.txt"`.

## Exemple d'utilisation

L'exemple ci-dessous montre comment lire à partir d'un fichier :
```c
lv_fs_file_t f;
lv_fs_res_t res;
res = lv_fs_open(&f, "S:folder/file.txt", LV_FS_MODE_RD);
if(res != LV_FS_RES_OK) my_error_handling();

uint32_t read_num;
uint8_t buf[8];
res = lv_fs_read(&f, buf, 8, &read_num);
if(res != LV_FS_RES_OK || read_num != 8) my_error_handling();

lv_fs_close(&f);
```
*Le mode dans `lv_fs_open` peut être `LV_FS_MODE_WR` pour ouvrir en écriture ou `LV_FS_MODE_RD | LV_FS_MODE_WR` pour lecture/écriture*

Cet exemple montre comment lire le contenu d'un répertoire. Il appartient au pilote de marquer les répertoires, mais il peut être judicieux d’insérer un "/" devant le nom du répertoire.
```c
lv_fs_dir_t dir;
lv_fs_res_t res;
res = lv_fs_dir_open(&dir, "S:/folder");
if(res != LV_FS_RES_OK) my_error_handling();

char fn[256];
while(1) {
    res = lv_fs_dir_read(&dir, fn);
    if(res != LV_FS_RES_OK) {
        my_error_handling();
        break;
    }

    /* fn est vide s'il n'y a plus d'entrée à lire */
    if(strlen(fn) == 0) {
        break;
    }

    printf("%s\n", fn);
}

lv_fs_dir_close(&dir);
```

## Utiliser les pilotes pour les images

Les objets [Image](/object-types/img) peuvent également être ouverts à partir de fichiers (en plus des variables stockées dans la mémoire Flash)

Pour initialiser un pilote pour les images, les fonction de rappel suivantes sont requises :
- open
- close
- read
- seek
- tell


## API 

```eval_rst

.. doxygenfile:: lv_fs.h
  :project: lvgl
        
```


