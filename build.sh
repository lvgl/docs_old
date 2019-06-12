#HTML
gwtc --format html --title "LittlevGL documentation"  --css external.css --output . --file-name index ./locale/en
google-chrome index.html
exit 0

gwtc --format html --title "LittlevGL documentation" --output ./locale/pt_BR --file-name index ./locale/pt_BR
gwtc --format html --title "LittlevGL documentation" --output ./locale/tr --file-name index ./locale/tr
gwtc --format html --title "LittlevGL documentation" --output ./locale/es --file-name index ./locale/es 

desc='    <meta name="description" content="Learn how to Port LittlevGL to your embedded hardware or set-up a PC simulator and see how the library works to create widgets, set their appearance, create animations etc.">'
kw='    <meta name="keywords" content="littlev graphics library, littlevgl, software library, gui, free, open source, embedded gui, documentation, porting, pc simulator, widgets, objects">'
og='    <meta prefix="og: http://ogp.me/ns#" property="og:site_name" content="LittlevGL">'
favicon='    <link rel="icon" type="image/png" sizes="32x32" href="https://littlevgl.com/favicon/favicon-32.png">\n  <link rel="icon" type="image/png" sizes="16x16" "https://littlevgl.com/favicon/favicon-16.png">\n  <link rel="apple-touch-icon" sizes="180x180" href="https://littlevgl.com/favicon/apple-touch-icon.png">'
ga='<script async src="https://www.googletagmanager.com/gtag/js?id=UA-78811084-3"></script>\n<script>\n  window.dataLayer = window.dataLayer || [];\n  function gtag(){dataLayer.push(arguments);}\n  gtag("js", new Date());\n  gtag("config", "UA-78811084-3");\n</script>';

sed -i  "/<head>/a  $desc\n$kw\n$og\n$favicon\n$ga" index.html
sed -i  "/<head>/a  $desc\n$kw\n$og\n$favicon\n$ga" ./locale/tr/index.html
sed -i  "/<head>/a  $desc\n$kw\n$og\n$favicon\n$ga" ./locale/es/index.html
sed -i  "/<head>/a  $desc\n$kw\n$og\n$favicon\n$ga" ./locale/pt_BR/index.html

#PDF
gwtc --format pdf --pdf-page-count --title "LittlevGL documentation (English)"  --output ./pdf --file-name LittlevGL_documentation_English ./locale/en
gwtc --format pdf --pdf-page-count --title "LittlevGL documentation (Brazilian Portuguese)"  --output ./pdf --file-name LittlevGL_documentation_Brazilian_Portuguese ./locale/pt_BR
gwtc --format pdf --pdf-page-count --title "LittlevGL documentation (Turkish)"  --output ./pdf --file-name LittlevGL_documentation_Turkish ./locale/tr
gwtc --format pdf --pdf-page-count --title "LittlevGL documentation (Espanol)"  --output ./pdf --file-name LittlevGL_documentation_Espanol ./locale/es




