# 📊 SOTA Evaluation Results

> **Reference benchmarks for methods with available code/checkpoints.**
> *All metrics are in percentage (%).*

## 1. OCIM Protocols (Cross-Dataset)

<table>
  <tr>
    <th rowspan="2">Method</th>
    <th colspan="4" style="text-align:center">Oulu (ICMO)</th>
    <th colspan="4" style="text-align:center">Casia (OIMC)</th>
    <th colspan="4" style="text-align:center">MSU (OCIM)</th>
    <th colspan="4" style="text-align:center">Idiap (OCMI)</th>
  </tr>
  <tr>
    <th>EER (%)</th><th>AUC (%)</th><th>TPR@1%FPR (%)</th><th>TPR@5%FPR (%)</th>
    <th>EER (%)</th><th>AUC (%)</th><th>TPR@1%FPR (%)</th><th>TPR@5%FPR (%)</th>
    <th>EER (%)</th><th>AUC (%)</th><th>TPR@1%FPR (%)</th><th>TPR@5%FPR (%)</th>
    <th>EER (%)</th><th>AUC (%)</th><th>TPR@1%FPR (%)</th><th>TPR@5%FPR (%)</th>
  </tr>
  <tr>
    <td><a href="CF-FAS" class="internal-link">CF-FAS</a></td>
    <td>20.033</td><td>80.209</td><td>0.000</td><td>0.000</td>
    <td>13.851</td><td>89.742</td><td>0.000</td><td>67.894</td>
    <td>10.106</td><td>95.404</td><td>40.778</td><td>76.001</td>
    <td>19.095</td><td>82.174</td><td>32.671</td><td>57.931</td>
  </tr>
  <tr>
    <td><a href="DGUA-FAS" class="internal-link">DGUA-FAS</a></td>
    <td>14.681</td><td>93.762</td><td>46.934</td><td>70.354</td>
    <td>14.187</td><td>93.991</td><td>58.675</td><td>70.702</td>
    <td>10.646</td><td>96.003</td><td>50.942</td><td>81.682</td>
    <td>12.255</td><td>94.829</td><td>55.647</td><td>76.812</td>
  </tr>
  <tr>
    <td><a href="LMFD-FAS" class="internal-link">LMFD-FAS</a></td>
    <td>16.238</td><td>91.463</td><td>0.000</td><td>66.463</td>
    <td>25.730</td><td>82.627</td><td>23.751</td><td>48.897</td>
    <td>18.239</td><td>90.319</td><td>25.413</td><td>47.869</td>
    <td>19.249</td><td>88.687</td><td>27.884</td><td>50.916</td>
  </tr>
  <tr>
    <td><a href="FLIP-FAS" class="internal-link">FLIP-FAS</a></td>
    <td><b>5.522</b></td><td><b>98.643</b></td><td><b>83.058</b></td><td><b>94.028</b></td>
    <td><b>4.080</b></td><td><b>99.258</b></td><td><b>83.772</b></td><td><b>97.111</b></td>
    <td>10.331</td><td>95.855</td><td><b>63.774</b></td><td><b>84.310</b></td>
    <td><b>3.141</b></td><td><b>99.633</b></td><td><b>91.368</b></td><td><b>98.449</b></td>
  </tr>
  <tr>
    <td><a href="JPD-FAS" class="internal-link">JPD-FAS</a></td>
    <td>5.470</td><td>98.641</td><td>70.897</td><td>93.853</td>
    <td>15.581</td><td>91.985</td><td>58.459</td><td>72.532</td>
    <td>16.393</td><td>91.987</td><td>36.796</td><td>64.788</td>
    <td>19.064</td><td>82.062</td><td>0.000</td><td>0.000</td>
  </tr>
  <tr>
    <td><a href="IADG-FAS" class="internal-link">IADG-FAS</a></td>
    <td>12.190</td><td>93.631</td><td>58.602</td><td>80.352</td>
    <td>16.711</td><td>91.038</td><td>26.219</td><td>58.753</td>
    <td>27.763</td><td>79.117</td><td>4.642</td><td>42.602</td>
    <td>41.141</td><td>61.424</td><td>0.448</td><td>6.765</td>
  </tr>
  <tr>
    <td><a href="GACD-FAS" class="internal-link">GACD-FAS</a></td>
    <td>9.776</td><td>96.692</td><td>52.938</td><td>81.558</td>
    <td>14.796</td><td>92.090</td><td>14.122</td><td>68.260</td>
    <td>10.409</td><td><b>96.653</b></td><td>51.242</td><td>83.251</td>
    <td>4.363</td><td>98.984</td><td>75.953</td><td>96.545</td>
  </tr>
</table>

## 2. Unseen Data: iPhone India
*Evaluation on proprietary dataset.*

<table>
  <tr>
    <th rowspan="2">Method</th>
    <th colspan="4" style="text-align:center">Protocol 1</th>
    <th colspan="4" style="text-align:center">Protocol 2</th>
    <th colspan="4" style="text-align:center">Protocol 3</th>
    <th colspan="4" style="text-align:center">Protocol 4</th>
  </tr>
  <tr>
    <th>EER (%)</th><th>AUC (%)</th><th>TPR@1%FPR (%)</th><th>TPR@5%FPR (%)</th>
    <th>EER (%)</th><th>AUC (%)</th><th>TPR@1%FPR (%)</th><th>TPR@5%FPR (%)</th>
    <th>EER (%)</th><th>AUC (%)</th><th>TPR@1%FPR (%)</th><th>TPR@5%FPR (%)</th>
    <th>EER (%)</th><th>AUC (%)</th><th>TPR@1%FPR (%)</th><th>TPR@5%FPR (%)</th>
  </tr>
  <tr>
    <td><a href="CF-FAS" class="internal-link">CF-FAS</a></td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
  </tr>
  <tr>
    <td><a href="DGUA-FAS" class="internal-link">DGUA-FAS</a></td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
  </tr>
  <tr>
    <td><a href="LMFD-FAS" class="internal-link">LMFD-FAS</a></td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
  </tr>
  <tr>
    <td><a href="FLIP-FAS" class="internal-link">FLIP-FAS</a></td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
  </tr>
  <tr>
    <td><a href="JPD-FAS" class="internal-link">JPD-FAS</a></td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
  </tr>
  <tr>
    <td><a href="IADG-FAS" class="internal-link">IADG-FAS</a></td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
  </tr>
  <tr>
    <td><a href="GACD-FAS" class="internal-link">GACD-FAS</a></td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
    <td>-</td><td>-</td><td>-</td><td>-</td>
  </tr>
</table>

---
Tags: #phd #sota #benchmark #results #metrics
