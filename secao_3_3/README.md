# Tabela Métodos de Leitura e Escrita Pandas

| Tipo de Dado            | Descrição do Dado           | Método para Leitura | Método para Escrita |
|-------------------------|-----------------------------|---------------------|---------------------|
| Texto                   | CSV                         | read_csv            | to_csv              |
| Texto                   | Fixe-width texto file        | read_fwf            |                     |
| Texto                   | JSON                        | read_json           | to_json             |
| Texto                   | HTML                        | read_html           | to_html             |
| Texto                   | Latex                       |                     | styler.to_latex     |
| Texto                   | XML                         | read_xml            | to_xml              |
| Texto                   | Local Clipboard             | read_clipboard      | to_clipboard        |
| Binário                 | MS Excel                    | read_excel          | to_excel            |
| Binário                 | OpenDocument                | read_excel          |                     |
| Binário                 | HDF5 Format                 | read_hdf            | to_hdf              |
| Binário                 | Feather Format              | read_feather        | to_feather          |
| Binário                 | Parquet Format              | read_parquet        | to_parquet          |
| Binário                 | ORC Format                  | read_orc            |                     |
| Binário                 | MsgPack                     | read_msgpack        | to_msgpack          |
| Binário                 | Stata                       | read_stata          | to_stata            |
| Binário                 | SAS                         | read_sas            |                     |
| Binário                 | SPSS                        | read_spss           |                     |
| Binário                 | Python Pickle Format        | read_pickle         | to_pickle           |
| SQL                     | SQL                         | read_sql            | to_sql              |
| SQL                     | Google BigQuery             | read_gbq            | to_gbq              |
