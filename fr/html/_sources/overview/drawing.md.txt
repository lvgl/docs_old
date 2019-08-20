```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/drawing.md
```
# Dessin

Avec LittlevGL, vous n'avez pas besoin de dessiner quoi que ce soit manuellement. Créez simplement des objets (comme des boutons et des étiquettes), déplacez-les et modifiez-les. LittlevGL actualisera et redessinera les éléments requis.

Cependant, il peut être utile d’avoir une compréhension de base de la façon dont le dessin est effectué dans LittlevGL.

Le concept de base est de ne pas dessiner directement à l'écran, mais d'abord dans un tampon interne, puis de le copier sur l'écran lorsque le rendu est prêt. Cela présente deux avantages principaux :
1. **Évite le scintillement** pendant que des couches de l'interface utilisateur sont dessinées. P.ex. lorsque vous dessinez un *arrière-plan + bouton + texte*, chaque "étape" sera visible pendant un court instant.
2. **C'est plus rapide**, car lorsque les pixels sont redessinés plusieurs fois (p.ex. arrière-plan + bouton + texte), il est plus rapide de modifier un tampon dans la MEV et d'écrire physiquement le pixel une seule fois
que de lire/écrire un affichage directement sur chaque accès pixel (p.ex. via un contrôleur d'affichage avec interface SPI).

## Types de tampons

Comme vous l'avez peut-être déjà appris dans la section [Portage](/porting/display), il existe 3 techniques d'utilisation de tampon :
1. **Un tampon** LittlevGL dessine le contenu de l'écran dans un tampon et l'envoie à l'affichage. Le tampon peut être plus petit que l'affichage. Dans ce cas, les zones les plus grandes seront redessinées en plusieurs parties. Si seules de petites zones changent (p.ex. appui sur un bouton), seules ces zones seront actualisées.
2. **Deux tampons de taille différente de l'écran** ayant deux tampons LittlevGL peut dessiner dans un tampon tandis que le contenu de l'autre tampon est envoyé à l’écran en arrière-plan.
Le DMA ou une autre méthode doit être utilisé pour transférer les données à l’écran afin de permettre au CPU de dessiner dans le même temps.
De cette manière, le rendu et le rafraîchissement de l'affichage deviennent parallèles. De même que pour *Un tampon*, LittlevGL dessine le contenu de l'affichage en fragments si le tampon est plus petit que la zone à actualiser.
3. **Deux tampons de la taille d'un écran**.
Contrairement à *Deux tampons de taille différente de l'écran* LittlevGL fournira toujours tout le contenu de l'affichage, pas seulement des fragments. De cette façon, le pilote peut simplement changer l'adresse du tampon d'affichage par celle du tampon préparé par LittlevGL.
Par conséquent, cette méthode est la meilleure lorsque le microcontrôleur dispose d’une interface LCD/TFT et que le tampon d'affichage est un emplacement dans la MEV.

## Mécanisme de rafraîchissement de l'écran

1. Quelque chose se passe dans l'interface graphique qui nécessite de redessiner. P.ex. un bouton a été pressé, un graphique a été modifié ou une animation s'est produite, etc.
2. LittlevGL enregistre l'ancienne et la nouvelle zone de l'objet modifié dans un tampon appelé *tampon de zone non valide*. Pour l'optimisation, dans certains cas, des objets ne sont pas ajoutés au tampon :
- Les objets cachés ne sont pas ajoutés
- Les objets complètement en-dehors de leur parent ne sont pas ajoutés
- Les zones partiellement hors du parent sont limitées à la zone du parent
- Les objets sur d'autres écrans ne sont pas ajoutés
3. A chaque `LV_DISP_DEF_REFR_PERIOD` (définie dans *lv_conf.h*) :
- LittlevGL vérifie les zones non valides et joint les zones adjacentes sécantes
- Prend la première zone jointe si elle est plus petite que le *tampon d'affichage*, puis dessine simplement le contenu de la zone dans la *tampon d'affichage*. Si la zone ne rentre pas dans le tampon, dessine autant de lignes que possible dans le *tampon d'affichage*.
- Quand la zone est dessinée, appelle `flush_cb` du pilote d'affichage pour actualiser l'affichage
- Si la zone était plus grande que le tampon, redessine également les parties restantes.
- Fait la même chose avec toutes les zones jointes.
 
Lorsqu'une zone est redessinée, la librairie recherche l'objet le plus haut couvrant la zone à redessiner et commence à dessiner à partir de cet objet.
Par exemple, si l'étiquette d'un bouton a changée, la librairie verra qu'il suffit de dessiner le bouton sous le texte et qu'il n'est pas nécessaire de dessiner l'arrière-plan également.
 
La différence entre les types de tampons en ce qui concerne le mécanisme de dessin est la suivante :
1. **Un tampon** LittlevGL doit attendre `lv_disp_flush_ready()` (appelée à la fin de `flush_cb`) avant de commencer à redessiner la partie suivante.
2. **Deux tampons de taille différente de l'écran** LittlevGL peut immédiatement utiliser le second tampon lorsque le premier est envoyé à `flush_cb` car le transfert doit être effectué par DMA (ou une autre méthode) en arrière-plan.
3. **Deux tampons de la taille de l'écran** Après avoir appelé `flush_cb`, un premier tampon est affiché. Son contenu est copié dans le second tampon et toutes les modifications sont dessinées dessus.
 
 
