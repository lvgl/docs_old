```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/log.md
```
# Journalisation

LittlevGL a un module *journal* intégré pour informer l'utilisateur de ce qui se passe dans la librairie.

## Niveau de détail
Pour activer la journalisation, définissez `LV_USE_LOG 1` dans *lv_conf.h* et définissez` LV_LOG_LEVEL` sur l'une des valeurs suivantes :
- **LV_LOG_LEVEL_TRACE** Beaucoup de messages pour donner des informations détaillées
- **LV_LOG_LEVEL_INFO**  Consigne les événements importants
- **LV_LOG_LEVEL_WARN**  Journalise si quelque chose d'inattendu s'est produit mais n'a pas causé de problème
- **LV_LOG_LEVEL_ERROR** Uniquement les problèmes critiques, lorsque le système peut planter
- **LV_LOG_LEVEL_NONE**  Ne journalise rien

Les événements dont le niveau est supérieur au niveau de journalisation défini seront également consignés. Par exemple si vous activez `LV_LOG_LEVEL_WARN`, *les erreurs* seront également consignées.

## Journalisation avec printf
Si votre système prend en charge `printf`, il vous suffit d'activer `LV_LOG_PRINTF` dans *lv_conf.h* pour traiter les journaux avec `printf`.


## Fonction de journalisation personnalisée
Si vous ne pouvez pas utiliser `printf` ou si vous souhaitez utiliser une fonction personnalisée pour journaliser, vous pouvez enregistrer une fonction de  rappel "journaliseur" avec `lv_log_register_print_cb() `.

Par exemple :

```c
void my_log_cb(lv_log_level_t level, const char * file, int line, const char * dsc)
{
  /* Envoie les messages via le port série */
  if(level == LV_LOG_LEVEL_ERROR) serial_send("ERROR: ");
  if(level == LV_LOG_LEVEL_WARN)  serial_send("WARNING: ");
  if(level == LV_LOG_LEVEL_INFO)  serial_send("INFO: ");
  if(level == LV_LOG_LEVEL_TRACE) serial_send("TRACE: ");

  serial_send("File: ");
  serial_send(file);

  char line_str[8];
  sprintf(line_str,"%d", line);
  serial_send("#");
  serial_send(line_str);

  serial_send(": ");
  serial_send(dsc);
  serial_send("\n");
}

...


lv_log_register_print_cb(my_log_cb);

```

## Ajouter des messages

Vous pouvez également utiliser le module de journalisation via les fonctions `LV_LOG_TRACE/INFO/WARN/ERROR(description)`.
