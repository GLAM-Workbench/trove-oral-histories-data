# trove-oral-histories-data

*A GLAM Workbench data repository*

These datasets were generated using notebooks in the [trove-music](https://github.com/GLAM-Workbench/trove-music/) repository.

For more information and documentation see the [Trove music, sound, and oral histories](https://glam-workbench.net/trove-music) section of the [GLAM Workbench](https://glam-workbench.net).

## Dataset summary
- [trove-oral-histories.csv](https://github.com/GLAM-Workbench/trove-oral-histories-data/blob/main/trove-oral-histories.csv) (15.1 MB, text/csv)
- [trove-oral-history-series.txt](https://github.com/GLAM-Workbench/trove-oral-histories-data/blob/main/trove-oral-history-series.txt) (86.0 kB, text/plain)


## Dataset details

### [trove-oral-histories.csv](https://github.com/GLAM-Workbench/trove-oral-histories-data/blob/main/trove-oral-histories.csv)


<table id="T_6ea86">
  <thead>
  </thead>
  <tbody>
    <tr>
      <th id="T_6ea86_level0_row0" class="row_heading level0 row0" >date harvested</th>
      <td id="T_6ea86_row0_col0" class="data row0 col0" >2023-12-15</td>
    </tr>
    <tr>
      <th id="T_6ea86_level0_row1" class="row_heading level0 row1" >file size</th>
      <td id="T_6ea86_row1_col0" class="data row1 col0" >15.1 MB</td>
    </tr>
    <tr>
      <th id="T_6ea86_level0_row2" class="row_heading level0 row2" >format</th>
      <td id="T_6ea86_row2_col0" class="data row2 col0" >text/csv</td>
    </tr>
    <tr>
      <th id="T_6ea86_level0_row3" class="row_heading level0 row3" >created by</th>
      <td id="T_6ea86_row3_col0" class="data row3 col0" ><a href='https://github.com/GLAM-Workbench/trove-music/blob/master/harvest-oral-histories.ipynb'>Harvest oral histories metadata</a></td>
    </tr>
    <tr>
      <th id="T_6ea86_level0_row4" class="row_heading level0 row4" >number of rows</th>
      <td id="T_6ea86_row4_col0" class="data row4 col0" >20,083</td>
    </tr>
  </tbody>
</table>


### Examples of use

- [Explore using Datasette](https://glam-workbench.net/datasette-lite/?csv=https://github.com/GLAM-Workbench/trove-oral-histories-data/blob/main/trove-oral-histories.csv&fts=title&fts=contributor&fts=is_part_of)
- [Visualised in the *Trove Data Guide*](https://tdg.glam-workbench.net/other-digitised-resources/oral-histories/overview.html)
### Columns

| name                | type    | description                                                                                                                                                                             |
|:--------------------|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `title`             | string  | title of the oral history                                                                                                                                                               |
| `contributor`       | string  | includes both interviewers and interviewees; multiple values separated by <code>&#124;</code> symbol                                                                                    |
| `publisher`         | string  | mostly empty but can include some publication details; multiple values separated by <code>&#124;</code> symbol                                                                          |
| `date`              | string  | date the oral history was recorded; multiple values separated by <code>&#124;</code> symbol                                                                                             |
| `type`              | string  | for example `performed music`, `spoken word`; multiple values separated by <code>&#124;</code> symbol                                                                                   |
| `format`            | string  | for example `Sound recording`, `online resource`; multiple values separated by <code>&#124;</code> symbol                                                                               |
| `extent`            | string  | usually number of files/reels/tapes, sometimes includes duration; multiple values separated by <code>&#124;</code> symbol                                                               |
| `language`          | string  | language of the recording; multiple values separated by <code>&#124;</code> symbol                                                                                                      |
| `subject`           | string  | subjects of interview; multiple values separated by <code>&#124;</code> symbol                                                                                                          |
| `spatial`           | string  | associated places (mostly using [Library of Congress geographic area codes](https://www.loc.gov/marc/geoareas/gacs_code.html)); multiple values separated by <code>&#124;</code> symbol |
| `is_part_of`        | string  | collections or projects that this interview belongs to; multiple values separated by <code>&#124;</code> symbol                                                                         |
| `identifier`        | string  | library identifiers; multiple values separated by <code>&#124;</code> symbol                                                                                                            |
| `rights`            | string  | copyright and licensing information; multiple values separated by <code>&#124;</code> symbol                                                                                            |
| `work_url`          | string  | link to work record in Trove; multiple values separated by <code>&#124;</code> symbol                                                                                                   |
| `work_type`         | string  | Trove work format, for example `Sound/Interview, lecture, talk`; multiple values separated by <code>&#124;</code> symbol                                                                |
| `fulltext_url`      | string  | link to audio player (if digitised)                                                                                                                                                     |
| `fulltext_url_text` | string  | text of link to audio player; multiple values separated by <code>&#124;</code> symbol                                                                                                   |
| `catalogue_url`     | string  | link to NLA catalogue entry; multiple values separated by <code>&#124;</code> symbol                                                                                                    |
| `summary`           | integer | text summary is available for download – `0` for no, `1` for yes                                                                                                                        |
| `transcript`        | integer | text transcript is available for download – `0` for no, `1` for yes                                                                                                                     |
| `sessions`          | integer | number of recording sessions                                                                                                                                                            |
| `duration`          | integer | total duration of recordings (in seconds)                                                                                                                                               |

### [trove-oral-history-series.txt](https://github.com/GLAM-Workbench/trove-oral-histories-data/blob/main/trove-oral-history-series.txt)


<table id="T_d2a5a">
  <thead>
  </thead>
  <tbody>
    <tr>
      <th id="T_d2a5a_level0_row0" class="row_heading level0 row0" >date harvested</th>
      <td id="T_d2a5a_row0_col0" class="data row0 col0" >2023-12-15</td>
    </tr>
    <tr>
      <th id="T_d2a5a_level0_row1" class="row_heading level0 row1" >file size</th>
      <td id="T_d2a5a_row1_col0" class="data row1 col0" >86.0 kB</td>
    </tr>
    <tr>
      <th id="T_d2a5a_level0_row2" class="row_heading level0 row2" >format</th>
      <td id="T_d2a5a_row2_col0" class="data row2 col0" >text/plain</td>
    </tr>
    <tr>
      <th id="T_d2a5a_level0_row3" class="row_heading level0 row3" >created by</th>
      <td id="T_d2a5a_row3_col0" class="data row3 col0" ><a href='https://github.com/GLAM-Workbench/trove-music/blob/master/save-series.ipynb'>Save a list of oral history collections</a></td>
    </tr>
  </tbody>
</table>




----
Created by [Tim Sherratt](https://timsherratt.au) for the [GLAM Workbench](https://glam-workbench.net)