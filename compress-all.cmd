SET PATH=c:\Soft\7-Zip\;%PATH%
PUSHD python-hana
call compress.cmd
POPD
PUSHD python-pdf-tables
call compress.cmd
POPD
RM uol-data-analytics.zip
7z a -tzip uol-data-analytics.zip python-pdf-tables/archives/pdf-tables-converter-and-analysis.zip python-hana/archives/analytics-basics-with-sap-hana-and-python.zip README.html