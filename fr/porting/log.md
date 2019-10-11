```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/log.md
```
# Journalisation

LittlevGL a un module *journal* intégré pour informer l'utilisateur de ce qui se passe dans la librairie.

## Niveau de détail
To enable logging, set `LV_USE_LOG  1` in *lv_conf.h* and set `LV_LOG_LEVEL` to one of the following values:
- **LV_LOG_LEVEL_TRACE** Beaucoup de messages pour donner des informations détaillées
- **LV_LOG_LEVEL_INFO**  Consigne les événements importants
- **LV_LOG_LEVEL_WARN**  Journalise si quelque chose d'inattendu s'est produit mais n'a pas causé de problème
- **LV_LOG_LEVEL_ERROR** Uniquement les problèmes critiques, lorsque le système peut planter
- **LV_LOG_LEVEL_NONE**  Ne journalise rien

The events which have a higher level than the set log level will be logged too. E.g. if you `LV_LOG_LEVEL_WARN`, *errors* will be also logged.

## Journalisation avec printf
If your system supports `printf`, you just need to enable `LV_LOG_PRINTF` in *lv_conf.h* to send the logs with `printf`.


## Fonction de journalisation personnalisée
If you can't use `printf` or want to use a custom function to log, you can register a "logger" callback with `lv_log_register_print_cb()`. 

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
