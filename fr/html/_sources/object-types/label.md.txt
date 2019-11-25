```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/label.md
```
# Etiquette (lv_label)

## Vue d’ensemble
Les étiquettes sont les objets de base pour afficher du texte.

### Définir le texte
Vous pouvez modifier le texte en cours d’exécution à tout moment avec `lv_label_set_text(label, "Nouveau texte")`. Le texte sera alloué dynamiquement.

With `lv_label_set_text_fmt(label, "Value: %d", 15)`a **printf-like formatting** can used to set the text.

Les étiquettes peuvent afficher du texte à partir d'un **texte statique**. Utilisez `lv_label_set_static_text(label, text)`. 
Dans ce cas, le texte n'est pas enregistré dans la mémoire dynamique, mais le texte est utilisé directement.
Keep in mind that the array can't be a local variable which destroys when the function exits.

Vous pouvez également utiliser un **tableau de caractères** comme texte d'étiquette.
Le tableau ne doit pas obligatoirement être terminé par "\ 0". Dans ce cas, le texte sera enregistré dans la mémoire dynamique.
Pour définir un tableau de caractères, utilisez la fonction `lv_label_set_array_text(label, array)`.


### Saut de ligne
Vous pouvez utiliser `\n` pour faire un saut de ligne. Par exemple : `"ligne 1\nligne 2\n\nligne 4"`.

### Modes d'adaptation au texte
La taille de l'objet étiquette peut être automatiquement étendue à la taille du texte ou le texte peut être manipulé selon plusieurs règles de mode :

* **LV_LABEL_LONG_EXPAND** augmente la taille de l'objet à la taille du texte (par défaut),
* **LV_LABEL_LONG_BREAK** conserve la largeur de l'objet, découpe les lignes trop longues et augmente la hauteur de l'objet,
* **LV_LABEL_LONG_DOTS** conserve la taille de l'objet, découpe le texte et écrit des points en fin de dernière ligne,
* **LV_LABEL_LONG_SROLL** conserve la taille de l'objet et fait défiler le texte en avant et en arrière,
* **LV_LABEL_LONG_SROLL_CIRC** conserve la taille de l'objet et fait défiler le textede manière circulaire,
* **LV_LABEL_LONG_CROP** conserve la taille et coupe le texte en dehors.

Pour spécifier le mode d'adaptation au texte, utilisez `lv_label_set_long_mode(label, LV_LABEL_LONG_...)`

Il est important de noter que lorsqu'une étiquette est créée et que son texte est défini, la taille de l'étiquette est déjà étendue à la taille du texte.
L'utilisation des fonctions `lv_obj_set_width/height/size()` avec le *mode d'adaptation du texte* par défaut `LV_LABEL_LONG_EXPAND` ne produit aucun effet.
Vous devez donc d'abord changer le *mode d'adaptation du texte* puis définir la taille avec `lv_obj_set_width/height/size()`.

### Alignement du texte
Le texte de l'étiquette peut être aligné à gauche, à droite ou au milieu avec `lv_label_set_align(label, LV_LABEL_ALIGN_LEFT/RIGHT/CENTER)`

### Dessin d'arrière-plan
Vous pouvez activer le dessin de l’arrière-plan de l’étiquette avec `lv_label_set_body_draw(label, draw)`

L’arrière-plan sera plus grand dans toutes les directions  de la valeur de `body.padding.top/bottom/left/right`.
Cependant, l'arrière-plan n'est dessiné que "virtuellement" et ne rend pas l'étiquette plus grande.
Par conséquent, lorsque l'étiquette est positionnée, les coordonnées de l'étiquette sont prises en compte et non celles de l'arrière-plan.

### Coloration du texte
Dans le texte, vous pouvez utiliser des commandes pour colorer des parties du texte. Par exemple : `"Ecrire un mot #ff0000 rouge#"`. 
Cette fonctionnalité peut être activée individuellement pour chaque étiquette à l’aide de la fonction `lv_label_set_recolor()`.

Notez que la coloration ne fonctionne que sur une seule ligne. C.-à-d. il ne peut pas y avoir de `\n` dans le texte ou il ne peut être formaté par `LV_LABEL_LONG_BREAK`, sinon le texte de la nouvelle ligne ne sera pas coloré.

### Très long textes
LittlevGL peut gérer efficacement les très longs textes (> 40k caractères) en enregistrant des données supplémentaires (environ 12 octets) pour accélérer le dessin. Pour activer cette fonctionnalité, définissez `LV_LABEL_LONG_TXT_HINT 1` dans *lv_conf.h*.

### Symboles
Les étiquettes peuvent afficher des symboles en plus des lettres. Lisez la section [police](/overview/police) pour en savoir plus sur les symboles.

## Styles
Les étiquettes utilisent un style qui peut être défini par `lv_label_set_style(label, LV_LABEL_STYLE_MAIN, &style)`. A partir du style, les propriétés suivantes sont utilisées :
* toutes les propriétés de `style.text`,
* pour le dessin de l'arrière-plan les propriétés de `style.body`. `padding` n'augmentera la taille que de manière visuelle, la taille de l'objet réel ne sera pas modifiée.

Le style par défaut des étiquettes est `NULL`. Elles héritent donc du style du parent.

## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_label/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_label.h
  :project: lvgl
        
```

