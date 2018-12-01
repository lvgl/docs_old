#HTML
gwtc --format html --title "LittlevGL documentation" --output . --file-name index .
gwtc --format html --title "LittlevGL documentation" --output ./locale/tr --file-name index ./locale/tr
gwtc --format html --title "LittlevGL documentation" --output ./locale/es --file-name index ./locale/es 

#PDF
gwtc --format pdf --pdf-page-count --title "LittlevGL documentation (English)"  --output ./pdf --file-name LittlevGL_documentation_English ./
gwtc --format pdf --pdf-page-count --title "LittlevGL documentation (Turkish)"  --output ./pdf --file-name LittlevGL_documentation_Turkish ./locale/tr
gwtc --format pdf --pdf-page-count --title "LittlevGL documentation (Espanol)"  --output ./pdf --file-name LittlevGL_documentation_Espanol ./locale/es
