 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 1
  ➤ Train window: 2020-05-04 to 2020-11-04 — 184 days
  ➤ Val window  : 2020-11-04 to 2021-01-04   — 61 days
  ➤ Trade window: 2021-01-04 to 2021-03-04 — 59 days
count    60.000000
mean      0.014905
std       0.037071
min      -0.083952
25%      -0.008187
50%       0.011502
75%       0.038438
max       0.100382
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1278 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1073         |
|    iterations           | 2            |
|    time_elapsed         | 3            |
|    total_timesteps      | 4096         |
| train/                  |              |
|    approx_kl            | 0.0024697143 |
|    clip_fraction        | 0.00679      |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.85        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0272      |
|    n_updates            | 10           |
|    policy_gradient_loss | -0.000755    |
|    std                  | 1.01         |
|    value_loss           | 0.00834      |
------------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1005        |
|    iterations           | 3           |
|    time_elapsed         | 6           |
|    total_timesteps      | 6144        |
| train/                  |             |
|    approx_kl            | 0.004091392 |
|    clip_fraction        | 0.0349      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.86       |
|    explained_variance   | 0.0         |
|    learning_rate        | 0.00025     |
|    loss                 | -0.0307     |
|    n_updates            | 20          |
|    policy_gradient_loss | -0.0025     |
|    std                  | 1.01        |
|    value_loss           | 0.00484     |
-----------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 998          |
|    iterations           | 4            |
|    time_elapsed         | 8            |
|    total_timesteps      | 8192         |
| train/                  |              |
|    approx_kl            | 0.0045087403 |
|    clip_fraction        | 0.0214       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.86        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0177      |
|    n_updates            | 30           |
|    policy_gradient_loss | -0.00101     |
|    std                  | 1.01         |
|    value_loss           | 0.00291      |
------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1002         |
|    iterations           | 5            |
|    time_elapsed         | 10           |
|    total_timesteps      | 10240        |
| train/                  |              |
|    approx_kl            | 0.0033169007 |
|    clip_fraction        | 0.0108       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.85        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0249      |
|    n_updates            | 40           |
|    policy_gradient_loss | -0.000682    |
|    std                  | 1            |
|    value_loss           | 0.0016       |
------------------------------------------
--------------------------------------------
| time/                   |                |
|    fps                  | 962            |
|    iterations           | 6              |
|    time_elapsed         | 12             |
|    total_timesteps      | 12288          |
| train/                  |                |
|    approx_kl            | 0.0030892694   |
|    clip_fraction        | 0.0249         |
|    clip_range           | 0.2            |
|    entropy_loss         | -2.84          |
|    explained_variance   | -1.1920929e-07 |
|    learning_rate        | 0.00025        |
|    loss                 | -0.0296        |
|    n_updates            | 50             |
|    policy_gradient_loss | -0.00184       |
|    std                  | 0.996          |
|    value_loss           | 0.000933       |
--------------------------------------------
🔍 Sample PPO action: [[-0.09074833 -0.07827059]]

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ppo Sharpe: nan
ppo Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
a2c Sharpe: nan
a2c Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ddpg Sharpe: nan
ddpg Account Value Range: 1000000.00 to 1000000.00
 Best model: {best_model.__class__.__name__} with Sharpe {best_sharpe:.2f}
❌ No valid model selected — all Sharpe ratios were NaN or invalid.
No results to analyze.
 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 2
  ➤ Train window: 2020-08-04 to 2021-02-04 — 184 days
  ➤ Val window  : 2021-02-04 to 2021-04-04   — 59 days
  ➤ Trade window: 2021-04-04 to 2021-06-04 — 61 days
count    58.000000
mean      0.008346
std       0.044883
min      -0.096596
25%      -0.016296
50%       0.002865
75%       0.028754
max       0.190998
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1409 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1173        |
|    iterations           | 2           |
|    time_elapsed         | 3           |
|    total_timesteps      | 4096        |
| train/                  |             |
|    approx_kl            | 0.004712173 |
|    clip_fraction        | 0.0323      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.83       |
|    explained_variance   | 0.24075669  |
|    learning_rate        | 0.00025     |
|    loss                 | -0.0304     |
|    n_updates            | 10          |
|    policy_gradient_loss | -0.00235    |
|    std                  | 0.995       |
|    value_loss           | 0.0175      |
-----------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1157         |
|    iterations           | 3            |
|    time_elapsed         | 5            |
|    total_timesteps      | 6144         |
| train/                  |              |
|    approx_kl            | 0.0042652665 |
|    clip_fraction        | 0.0139       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.83        |
|    explained_variance   | 0.8565376    |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0253      |
|    n_updates            | 20           |
|    policy_gradient_loss | -0.000914    |
|    std                  | 0.997        |
|    value_loss           | 0.00752      |
------------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1136        |
|    iterations           | 4           |
|    time_elapsed         | 7           |
|    total_timesteps      | 8192        |
| train/                  |             |
|    approx_kl            | 0.001554347 |
|    clip_fraction        | 0.0146      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.83       |
|    explained_variance   | 0.8998588   |
|    learning_rate        | 0.00025     |
|    loss                 | -0.0289     |
|    n_updates            | 30          |
|    policy_gradient_loss | -0.00112    |
|    std                  | 0.99        |
|    value_loss           | 0.00551     |
-----------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1134         |
|    iterations           | 5            |
|    time_elapsed         | 9            |
|    total_timesteps      | 10240        |
| train/                  |              |
|    approx_kl            | 0.0043944526 |
|    clip_fraction        | 0.0301       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.82        |
|    explained_variance   | 0.8813344    |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0354      |
|    n_updates            | 40           |
|    policy_gradient_loss | -0.00236     |
|    std                  | 0.992        |
|    value_loss           | 0.00361      |
------------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1119        |
|    iterations           | 6           |
|    time_elapsed         | 10          |
|    total_timesteps      | 12288       |
| train/                  |             |
|    approx_kl            | 0.006557583 |
|    clip_fraction        | 0.0582      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.81       |
|    explained_variance   | 0.86101985  |
|    learning_rate        | 0.00025     |
|    loss                 | -0.0298     |
|    n_updates            | 50          |
|    policy_gradient_loss | -0.00469    |
|    std                  | 0.985       |
|    value_loss           | 0.00242     |
-----------------------------------------
🔍 Sample PPO action: [[0.51006484 0.16634734]]

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ppo Sharpe: nan
ppo Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
a2c Sharpe: nan
a2c Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ddpg Sharpe: nan
ddpg Account Value Range: 1000000.00 to 1000000.00
 Best model: {best_model.__class__.__name__} with Sharpe {best_sharpe:.2f}
❌ No valid model selected — all Sharpe ratios were NaN or invalid.
No results to analyze.
 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 3
  ➤ Train window: 2020-11-04 to 2021-05-04 — 181 days
  ➤ Val window  : 2021-05-04 to 2021-07-04   — 61 days
  ➤ Trade window: 2021-07-04 to 2021-09-04 — 62 days
count    60.000000
mean     -0.005489
std       0.056171
min      -0.153507
25%      -0.040133
50%      -0.006630
75%       0.026712
max       0.127697
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1406 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1250         |
|    iterations           | 2            |
|    time_elapsed         | 3            |
|    total_timesteps      | 4096         |
| train/                  |              |
|    approx_kl            | 0.0028017852 |
|    clip_fraction        | 0.0212       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.83        |
|    explained_variance   | -0.8852228   |
|    learning_rate        | 0.00025      |
|    loss                 | -0.031       |
|    n_updates            | 10           |
|    policy_gradient_loss | -0.00168     |
|    std                  | 0.994        |
|    value_loss           | 0.00347      |
------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1194         |
|    iterations           | 3            |
|    time_elapsed         | 5            |
|    total_timesteps      | 6144         |
| train/                  |              |
|    approx_kl            | 0.0030891092 |
|    clip_fraction        | 0.0176       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.82        |
|    explained_variance   | -0.3788123   |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0253      |
|    n_updates            | 20           |
|    policy_gradient_loss | -0.0017      |
|    std                  | 0.986        |
|    value_loss           | 0.00149      |
------------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1147        |
|    iterations           | 4           |
|    time_elapsed         | 7           |
|    total_timesteps      | 8192        |
| train/                  |             |
|    approx_kl            | 0.004755563 |
|    clip_fraction        | 0.0203      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.8        |
|    explained_variance   | 0.35451382  |
|    learning_rate        | 0.00025     |
|    loss                 | -0.0291     |
|    n_updates            | 30          |
|    policy_gradient_loss | -0.00141    |
|    std                  | 0.977       |
|    value_loss           | 0.000653    |
-----------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1136        |
|    iterations           | 5           |
|    time_elapsed         | 9           |
|    total_timesteps      | 10240       |
| train/                  |             |
|    approx_kl            | 0.004535647 |
|    clip_fraction        | 0.0465      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.79       |
|    explained_variance   | 0.6497601   |
|    learning_rate        | 0.00025     |
|    loss                 | -0.0303     |
|    n_updates            | 40          |
|    policy_gradient_loss | -0.0036     |
|    std                  | 0.975       |
|    value_loss           | 0.000366    |
-----------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1125         |
|    iterations           | 6            |
|    time_elapsed         | 10           |
|    total_timesteps      | 12288        |
| train/                  |              |
|    approx_kl            | 0.0023104683 |
|    clip_fraction        | 0.00205      |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.79        |
|    explained_variance   | 0.7315674    |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0343      |
|    n_updates            | 50           |
|    policy_gradient_loss | 1.33e-05     |
|    std                  | 0.975        |
|    value_loss           | 0.000193     |
------------------------------------------
🔍 Sample PPO action: [[-0.06201195  0.29175422]]

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ppo Sharpe: nan
ppo Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
a2c Sharpe: nan
a2c Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ddpg Sharpe: nan
ddpg Account Value Range: 1000000.00 to 1000000.00
 Best model: {best_model.__class__.__name__} with Sharpe {best_sharpe:.2f}
❌ No valid model selected — all Sharpe ratios were NaN or invalid.
No results to analyze.
 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 4
  ➤ Train window: 2021-02-04 to 2021-08-04 — 181 days
  ➤ Val window  : 2021-08-04 to 2021-10-04   — 61 days
  ➤ Trade window: 2021-10-04 to 2021-12-04 — 61 days
count    60.000000
mean      0.003979
std       0.038041
min      -0.111191
25%      -0.020156
50%       0.002880
75%       0.027307
max       0.098811
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1397 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1106         |
|    iterations           | 2            |
|    time_elapsed         | 3            |
|    total_timesteps      | 4096         |
| train/                  |              |
|    approx_kl            | 0.0062483265 |
|    clip_fraction        | 0.0569       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.83        |
|    explained_variance   | -0.45554626  |
|    learning_rate        | 0.00025      |
|    loss                 | -0.028       |
|    n_updates            | 10           |
|    policy_gradient_loss | -0.00308     |
|    std                  | 0.994        |
|    value_loss           | 0.00577      |
------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1092         |
|    iterations           | 3            |
|    time_elapsed         | 5            |
|    total_timesteps      | 6144         |
| train/                  |              |
|    approx_kl            | 0.0036769123 |
|    clip_fraction        | 0.00381      |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.82        |
|    explained_variance   | -0.1846093   |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0217      |
|    n_updates            | 20           |
|    policy_gradient_loss | -0.000232    |
|    std                  | 0.992        |
|    value_loss           | 0.00294      |
------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1046         |
|    iterations           | 4            |
|    time_elapsed         | 7            |
|    total_timesteps      | 8192         |
| train/                  |              |
|    approx_kl            | 0.0033954307 |
|    clip_fraction        | 0.0235       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.82        |
|    explained_variance   | -0.07512891  |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0376      |
|    n_updates            | 30           |
|    policy_gradient_loss | -0.00134     |
|    std                  | 0.992        |
|    value_loss           | 0.00167      |
------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1062         |
|    iterations           | 5            |
|    time_elapsed         | 9            |
|    total_timesteps      | 10240        |
| train/                  |              |
|    approx_kl            | 0.005050015  |
|    clip_fraction        | 0.0392       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.82        |
|    explained_variance   | -0.008525372 |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0338      |
|    n_updates            | 40           |
|    policy_gradient_loss | -0.00243     |
|    std                  | 0.991        |
|    value_loss           | 0.00106      |
------------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1054        |
|    iterations           | 6           |
|    time_elapsed         | 11          |
|    total_timesteps      | 12288       |
| train/                  |             |
|    approx_kl            | 0.005505005 |
|    clip_fraction        | 0.0349      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.82       |
|    explained_variance   | 0.017185807 |
|    learning_rate        | 0.00025     |
|    loss                 | -0.00705    |
|    n_updates            | 50          |
|    policy_gradient_loss | -0.0025     |
|    std                  | 0.987       |
|    value_loss           | 0.000528    |
-----------------------------------------
🔍 Sample PPO action: [[ 0.3098266  -0.34966058]]

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ppo Sharpe: nan
ppo Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
a2c Sharpe: nan
a2c Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ddpg Sharpe: nan
ddpg Account Value Range: 1000000.00 to 1000000.00
 Best model: {best_model.__class__.__name__} with Sharpe {best_sharpe:.2f}
❌ No valid model selected — all Sharpe ratios were NaN or invalid.
No results to analyze.
 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 5
  ➤ Train window: 2021-05-04 to 2021-11-04 — 184 days
  ➤ Val window  : 2021-11-04 to 2022-01-04   — 61 days
  ➤ Trade window: 2022-01-04 to 2022-03-04 — 59 days
count    60.000000
mean     -0.003994
std       0.032670
min      -0.090060
25%      -0.018657
50%      -0.000892
75%       0.015877
max       0.065516
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1421 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1260        |
|    iterations           | 2           |
|    time_elapsed         | 3           |
|    total_timesteps      | 4096        |
| train/                  |             |
|    approx_kl            | 0.002994482 |
|    clip_fraction        | 0.0161      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.84       |
|    explained_variance   | -0.40403545 |
|    learning_rate        | 0.00025     |
|    loss                 | -0.00905    |
|    n_updates            | 10          |
|    policy_gradient_loss | -0.000597   |
|    std                  | 0.998       |
|    value_loss           | 0.0309      |
-----------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1217         |
|    iterations           | 3            |
|    time_elapsed         | 5            |
|    total_timesteps      | 6144         |
| train/                  |              |
|    approx_kl            | 0.0041065477 |
|    clip_fraction        | 0.0337       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.83        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0206      |
|    n_updates            | 20           |
|    policy_gradient_loss | -0.00233     |
|    std                  | 0.993        |
|    value_loss           | 0.0205       |
------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1165         |
|    iterations           | 4            |
|    time_elapsed         | 7            |
|    total_timesteps      | 8192         |
| train/                  |              |
|    approx_kl            | 0.0027611568 |
|    clip_fraction        | 0.0103       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.83        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0254      |
|    n_updates            | 30           |
|    policy_gradient_loss | -0.00089     |
|    std                  | 0.998        |
|    value_loss           | 0.0116       |
------------------------------------------
--------------------------------------------
| time/                   |                |
|    fps                  | 1104           |
|    iterations           | 5              |
|    time_elapsed         | 9              |
|    total_timesteps      | 10240          |
| train/                  |                |
|    approx_kl            | 0.0022447784   |
|    clip_fraction        | 0.00659        |
|    clip_range           | 0.2            |
|    entropy_loss         | -2.83          |
|    explained_variance   | -1.1920929e-07 |
|    learning_rate        | 0.00025        |
|    loss                 | -0.0345        |
|    n_updates            | 40             |
|    policy_gradient_loss | -0.000653      |
|    std                  | 0.994          |
|    value_loss           | 0.00671        |
--------------------------------------------
-------------------------------------------
| time/                   |               |
|    fps                  | 1108          |
|    iterations           | 6             |
|    time_elapsed         | 11            |
|    total_timesteps      | 12288         |
| train/                  |               |
|    approx_kl            | 0.0047396524  |
|    clip_fraction        | 0.0254        |
|    clip_range           | 0.2           |
|    entropy_loss         | -2.84         |
|    explained_variance   | 5.9604645e-08 |
|    learning_rate        | 0.00025       |
|    loss                 | -0.0303       |
|    n_updates            | 50            |
|    policy_gradient_loss | -0.00106      |
|    std                  | 1             |
|    value_loss           | 0.00385       |
-------------------------------------------
🔍 Sample PPO action: [[-0.51817775 -0.43552765]]

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ppo Sharpe: nan
ppo Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
a2c Sharpe: nan
a2c Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ddpg Sharpe: nan
ddpg Account Value Range: 1000000.00 to 1000000.00
 Best model: {best_model.__class__.__name__} with Sharpe {best_sharpe:.2f}
❌ No valid model selected — all Sharpe ratios were NaN or invalid.
No results to analyze.
 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 6
  ➤ Train window: 2021-08-04 to 2022-02-04 — 184 days
  ➤ Val window  : 2022-02-04 to 2022-04-04   — 59 days
  ➤ Trade window: 2022-04-04 to 2022-06-04 — 61 days
count    58.000000
mean      0.002574
std       0.035689
min      -0.077664
25%      -0.017083
50%       0.002126
75%       0.021689
max       0.142998
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1392 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1090         |
|    iterations           | 2            |
|    time_elapsed         | 3            |
|    total_timesteps      | 4096         |
| train/                  |              |
|    approx_kl            | 0.0024243086 |
|    clip_fraction        | 0.0161       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.84        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | 0.0111       |
|    n_updates            | 10           |
|    policy_gradient_loss | -0.000798    |
|    std                  | 1            |
|    value_loss           | 0.081        |
------------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1087        |
|    iterations           | 3           |
|    time_elapsed         | 5           |
|    total_timesteps      | 6144        |
| train/                  |             |
|    approx_kl            | 0.005263291 |
|    clip_fraction        | 0.0464      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.84       |
|    explained_variance   | 0.0         |
|    learning_rate        | 0.00025     |
|    loss                 | 0.00214     |
|    n_updates            | 20          |
|    policy_gradient_loss | -0.00304    |
|    std                  | 1           |
|    value_loss           | 0.0469      |
-----------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1078        |
|    iterations           | 4           |
|    time_elapsed         | 7           |
|    total_timesteps      | 8192        |
| train/                  |             |
|    approx_kl            | 0.004621859 |
|    clip_fraction        | 0.0182      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.85       |
|    explained_variance   | 0.0         |
|    learning_rate        | 0.00025     |
|    loss                 | -0.0174     |
|    n_updates            | 30          |
|    policy_gradient_loss | -0.00157    |
|    std                  | 1.01        |
|    value_loss           | 0.0298      |
-----------------------------------------
-------------------------------------------
| time/                   |               |
|    fps                  | 1087          |
|    iterations           | 5             |
|    time_elapsed         | 9             |
|    total_timesteps      | 10240         |
| train/                  |               |
|    approx_kl            | 0.0044065174  |
|    clip_fraction        | 0.0224        |
|    clip_range           | 0.2           |
|    entropy_loss         | -2.85         |
|    explained_variance   | 1.1920929e-07 |
|    learning_rate        | 0.00025       |
|    loss                 | -0.0347       |
|    n_updates            | 40            |
|    policy_gradient_loss | -0.00103      |
|    std                  | 1             |
|    value_loss           | 0.0177        |
-------------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1093        |
|    iterations           | 6           |
|    time_elapsed         | 11          |
|    total_timesteps      | 12288       |
| train/                  |             |
|    approx_kl            | 0.002896093 |
|    clip_fraction        | 0.00625     |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.84       |
|    explained_variance   | 0.0         |
|    learning_rate        | 0.00025     |
|    loss                 | -0.0134     |
|    n_updates            | 50          |
|    policy_gradient_loss | -0.000485   |
|    std                  | 0.999       |
|    value_loss           | 0.0106      |
-----------------------------------------
🔍 Sample PPO action: [[-1.          0.04658091]]

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ppo Sharpe: nan
ppo Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
a2c Sharpe: nan
a2c Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ddpg Sharpe: nan
ddpg Account Value Range: 1000000.00 to 1000000.00
 Best model: {best_model.__class__.__name__} with Sharpe {best_sharpe:.2f}
❌ No valid model selected — all Sharpe ratios were NaN or invalid.
No results to analyze.
 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 7
  ➤ Train window: 2021-11-04 to 2022-05-04 — 181 days
  ➤ Val window  : 2022-05-04 to 2022-07-04   — 61 days
  ➤ Trade window: 2022-07-04 to 2022-09-04 — 62 days
count    60.000000
mean     -0.011257
std       0.043470
min      -0.153953
25%      -0.033011
50%      -0.007617
75%       0.012759
max       0.086979
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1310 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1209         |
|    iterations           | 2            |
|    time_elapsed         | 3            |
|    total_timesteps      | 4096         |
| train/                  |              |
|    approx_kl            | 0.0059449035 |
|    clip_fraction        | 0.0333       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.84        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0314      |
|    n_updates            | 10           |
|    policy_gradient_loss | -0.00163     |
|    std                  | 1            |
|    value_loss           | 0.00256      |
------------------------------------------
--------------------------------------------
| time/                   |                |
|    fps                  | 1176           |
|    iterations           | 3              |
|    time_elapsed         | 5              |
|    total_timesteps      | 6144           |
| train/                  |                |
|    approx_kl            | 0.0063098716   |
|    clip_fraction        | 0.0607         |
|    clip_range           | 0.2            |
|    entropy_loss         | -2.84          |
|    explained_variance   | -1.1920929e-07 |
|    learning_rate        | 0.00025        |
|    loss                 | -0.0327        |
|    n_updates            | 20             |
|    policy_gradient_loss | -0.00365       |
|    std                  | 1              |
|    value_loss           | 0.00155        |
--------------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1171        |
|    iterations           | 4           |
|    time_elapsed         | 6           |
|    total_timesteps      | 8192        |
| train/                  |             |
|    approx_kl            | 0.003021256 |
|    clip_fraction        | 0.0117      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.85       |
|    explained_variance   | 0.0         |
|    learning_rate        | 0.00025     |
|    loss                 | -0.0234     |
|    n_updates            | 30          |
|    policy_gradient_loss | -0.000512   |
|    std                  | 1.01        |
|    value_loss           | 0.000872    |
-----------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1168         |
|    iterations           | 5            |
|    time_elapsed         | 8            |
|    total_timesteps      | 10240        |
| train/                  |              |
|    approx_kl            | 0.0041547115 |
|    clip_fraction        | 0.0344       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.85        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0254      |
|    n_updates            | 40           |
|    policy_gradient_loss | -0.00255     |
|    std                  | 1.01         |
|    value_loss           | 0.00055      |
------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1156         |
|    iterations           | 6            |
|    time_elapsed         | 10           |
|    total_timesteps      | 12288        |
| train/                  |              |
|    approx_kl            | 0.0057797916 |
|    clip_fraction        | 0.0363       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.85        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0251      |
|    n_updates            | 50           |
|    policy_gradient_loss | -0.00217     |
|    std                  | 1            |
|    value_loss           | 0.00028      |
------------------------------------------
🔍 Sample PPO action: [[0.09129392 0.60673237]]

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ppo Sharpe: nan
ppo Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
a2c Sharpe: nan
a2c Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ddpg Sharpe: nan
ddpg Account Value Range: 1000000.00 to 1000000.00
 Best model: {best_model.__class__.__name__} with Sharpe {best_sharpe:.2f}
❌ No valid model selected — all Sharpe ratios were NaN or invalid.
No results to analyze.
 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 8
  ➤ Train window: 2022-02-04 to 2022-08-04 — 181 days
  ➤ Val window  : 2022-08-04 to 2022-10-04   — 61 days
  ➤ Trade window: 2022-10-04 to 2022-12-04 — 61 days
count    60.000000
mean     -0.001927
std       0.031454
min      -0.103612
25%      -0.011112
50%      -0.002226
75%       0.013144
max       0.101321
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1325 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1126         |
|    iterations           | 2            |
|    time_elapsed         | 3            |
|    total_timesteps      | 4096         |
| train/                  |              |
|    approx_kl            | 0.0029099835 |
|    clip_fraction        | 0.0442       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.84        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0376      |
|    n_updates            | 10           |
|    policy_gradient_loss | -0.00289     |
|    std                  | 1            |
|    value_loss           | 0.00492      |
------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1055         |
|    iterations           | 3            |
|    time_elapsed         | 5            |
|    total_timesteps      | 6144         |
| train/                  |              |
|    approx_kl            | 0.0037802358 |
|    clip_fraction        | 0.0289       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.85        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0321      |
|    n_updates            | 20           |
|    policy_gradient_loss | -0.0025      |
|    std                  | 1.01         |
|    value_loss           | 0.00269      |
------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1006         |
|    iterations           | 4            |
|    time_elapsed         | 8            |
|    total_timesteps      | 8192         |
| train/                  |              |
|    approx_kl            | 0.0031255656 |
|    clip_fraction        | 0.0134       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.86        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0314      |
|    n_updates            | 30           |
|    policy_gradient_loss | -0.000458    |
|    std                  | 1.01         |
|    value_loss           | 0.00156      |
------------------------------------------
-------------------------------------------
| time/                   |               |
|    fps                  | 1005          |
|    iterations           | 5             |
|    time_elapsed         | 10            |
|    total_timesteps      | 10240         |
| train/                  |               |
|    approx_kl            | 0.0041627674  |
|    clip_fraction        | 0.0245        |
|    clip_range           | 0.2           |
|    entropy_loss         | -2.87         |
|    explained_variance   | 5.9604645e-08 |
|    learning_rate        | 0.00025       |
|    loss                 | -0.0319       |
|    n_updates            | 40            |
|    policy_gradient_loss | -0.00293      |
|    std                  | 1.03          |
|    value_loss           | 0.000932      |
-------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1023         |
|    iterations           | 6            |
|    time_elapsed         | 12           |
|    total_timesteps      | 12288        |
| train/                  |              |
|    approx_kl            | 0.0033795433 |
|    clip_fraction        | 0.034        |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.9         |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0447      |
|    n_updates            | 50           |
|    policy_gradient_loss | -0.0041      |
|    std                  | 1.04         |
|    value_loss           | 0.000487     |
------------------------------------------
🔍 Sample PPO action: [[-1.          0.26977277]]

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ppo Sharpe: nan
ppo Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
a2c Sharpe: nan
a2c Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ddpg Sharpe: nan
ddpg Account Value Range: 1000000.00 to 1000000.00
 Best model: {best_model.__class__.__name__} with Sharpe {best_sharpe:.2f}
❌ No valid model selected — all Sharpe ratios were NaN or invalid.
No results to analyze.
 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 9
  ➤ Train window: 2022-05-04 to 2022-11-04 — 184 days
  ➤ Val window  : 2022-11-04 to 2023-01-04   — 61 days
  ➤ Trade window: 2023-01-04 to 2023-03-04 — 59 days
count    60.000000
mean     -0.003525
std       0.031491
min      -0.143671
25%      -0.013798
50%      -0.000906
75%       0.006221
max       0.110122
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1385 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1210        |
|    iterations           | 2           |
|    time_elapsed         | 3           |
|    total_timesteps      | 4096        |
| train/                  |             |
|    approx_kl            | 0.006197356 |
|    clip_fraction        | 0.0527      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.83       |
|    explained_variance   | 0.0         |
|    learning_rate        | 0.00025     |
|    loss                 | -0.0163     |
|    n_updates            | 10          |
|    policy_gradient_loss | -0.00334    |
|    std                  | 0.994       |
|    value_loss           | 0.0203      |
-----------------------------------------
-------------------------------------------
| time/                   |               |
|    fps                  | 1186          |
|    iterations           | 3             |
|    time_elapsed         | 5             |
|    total_timesteps      | 6144          |
| train/                  |               |
|    approx_kl            | 0.005278727   |
|    clip_fraction        | 0.0205        |
|    clip_range           | 0.2           |
|    entropy_loss         | -2.83         |
|    explained_variance   | 5.9604645e-08 |
|    learning_rate        | 0.00025       |
|    loss                 | -0.0125       |
|    n_updates            | 20            |
|    policy_gradient_loss | -0.000989     |
|    std                  | 0.994         |
|    value_loss           | 0.0123        |
-------------------------------------------
--------------------------------------------
| time/                   |                |
|    fps                  | 1176           |
|    iterations           | 4              |
|    time_elapsed         | 6              |
|    total_timesteps      | 8192           |
| train/                  |                |
|    approx_kl            | 0.0043213237   |
|    clip_fraction        | 0.0305         |
|    clip_range           | 0.2            |
|    entropy_loss         | -2.82          |
|    explained_variance   | -1.1920929e-07 |
|    learning_rate        | 0.00025        |
|    loss                 | -0.0325        |
|    n_updates            | 30             |
|    policy_gradient_loss | -0.00155       |
|    std                  | 0.991          |
|    value_loss           | 0.007          |
--------------------------------------------
--------------------------------------------
| time/                   |                |
|    fps                  | 1142           |
|    iterations           | 5              |
|    time_elapsed         | 8              |
|    total_timesteps      | 10240          |
| train/                  |                |
|    approx_kl            | 0.007350201    |
|    clip_fraction        | 0.0607         |
|    clip_range           | 0.2            |
|    entropy_loss         | -2.82          |
|    explained_variance   | -1.1920929e-07 |
|    learning_rate        | 0.00025        |
|    loss                 | -0.026         |
|    n_updates            | 40             |
|    policy_gradient_loss | -0.00435       |
|    std                  | 0.987          |
|    value_loss           | 0.0043         |
--------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1134         |
|    iterations           | 6            |
|    time_elapsed         | 10           |
|    total_timesteps      | 12288        |
| train/                  |              |
|    approx_kl            | 0.0029030433 |
|    clip_fraction        | 0.0153       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.82        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0288      |
|    n_updates            | 50           |
|    policy_gradient_loss | -0.00058     |
|    std                  | 0.997        |
|    value_loss           | 0.00234      |
------------------------------------------
🔍 Sample PPO action: [[-0.49770248 -0.3364169 ]]

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ppo Sharpe: nan
ppo Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
a2c Sharpe: nan
a2c Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ddpg Sharpe: nan
ddpg Account Value Range: 1000000.00 to 1000000.00
 Best model: {best_model.__class__.__name__} with Sharpe {best_sharpe:.2f}
❌ No valid model selected — all Sharpe ratios were NaN or invalid.
No results to analyze.
 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 10
  ➤ Train window: 2022-08-04 to 2023-02-04 — 184 days
  ➤ Val window  : 2023-02-04 to 2023-04-04   — 59 days
  ➤ Trade window: 2023-04-04 to 2023-06-04 — 61 days
count    58.000000
mean      0.003428
std       0.032316
min      -0.061894
25%      -0.013592
50%      -0.002238
75%       0.018283
max       0.094438
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1394 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
-------------------------------------------
| time/                   |               |
|    fps                  | 1129          |
|    iterations           | 2             |
|    time_elapsed         | 3             |
|    total_timesteps      | 4096          |
| train/                  |               |
|    approx_kl            | 0.0035926036  |
|    clip_fraction        | 0.0226        |
|    clip_range           | 0.2           |
|    entropy_loss         | -2.84         |
|    explained_variance   | 5.9604645e-08 |
|    learning_rate        | 0.00025       |
|    loss                 | -0.0185       |
|    n_updates            | 10            |
|    policy_gradient_loss | -0.0018       |
|    std                  | 1             |
|    value_loss           | 0.00399       |
-------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1095         |
|    iterations           | 3            |
|    time_elapsed         | 5            |
|    total_timesteps      | 6144         |
| train/                  |              |
|    approx_kl            | 0.0031560017 |
|    clip_fraction        | 0.025        |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.85        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0242      |
|    n_updates            | 20           |
|    policy_gradient_loss | -0.00145     |
|    std                  | 1.01         |
|    value_loss           | 0.00257      |
------------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1105        |
|    iterations           | 4           |
|    time_elapsed         | 7           |
|    total_timesteps      | 8192        |
| train/                  |             |
|    approx_kl            | 0.004929338 |
|    clip_fraction        | 0.0196      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.86       |
|    explained_variance   | 0.0         |
|    learning_rate        | 0.00025     |
|    loss                 | -0.0421     |
|    n_updates            | 30          |
|    policy_gradient_loss | -0.00132    |
|    std                  | 1.01        |
|    value_loss           | 0.00139     |
-----------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1111        |
|    iterations           | 5           |
|    time_elapsed         | 9           |
|    total_timesteps      | 10240       |
| train/                  |             |
|    approx_kl            | 0.004776079 |
|    clip_fraction        | 0.0214      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.86       |
|    explained_variance   | 0.0         |
|    learning_rate        | 0.00025     |
|    loss                 | -0.0247     |
|    n_updates            | 40          |
|    policy_gradient_loss | -0.00175    |
|    std                  | 1.01        |
|    value_loss           | 0.000835    |
-----------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1108         |
|    iterations           | 6            |
|    time_elapsed         | 11           |
|    total_timesteps      | 12288        |
| train/                  |              |
|    approx_kl            | 0.0042821732 |
|    clip_fraction        | 0.029        |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.86        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0107      |
|    n_updates            | 50           |
|    policy_gradient_loss | -0.00157     |
|    std                  | 1.01         |
|    value_loss           | 0.000488     |
------------------------------------------
🔍 Sample PPO action: [[-0.9677866  -0.45833278]]

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ppo Sharpe: nan
ppo Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
a2c Sharpe: nan
a2c Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ddpg Sharpe: nan
ddpg Account Value Range: 1000000.00 to 1000000.00
 Best model: {best_model.__class__.__name__} with Sharpe {best_sharpe:.2f}
❌ No valid model selected — all Sharpe ratios were NaN or invalid.
No results to analyze.
 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 11
  ➤ Train window: 2022-11-04 to 2023-05-04 — 181 days
  ➤ Val window  : 2023-05-04 to 2023-07-04   — 61 days
  ➤ Trade window: 2023-07-04 to 2023-09-04 — 62 days
count    60.000000
mean      0.001470
std       0.021117
min      -0.050561
25%      -0.008309
50%       0.001160
75%       0.009916
max       0.059237
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1306 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1066         |
|    iterations           | 2            |
|    time_elapsed         | 3            |
|    total_timesteps      | 4096         |
| train/                  |              |
|    approx_kl            | 0.0029222467 |
|    clip_fraction        | 0.00635      |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.83        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | 0.0249       |
|    n_updates            | 10           |
|    policy_gradient_loss | -0.000719    |
|    std                  | 0.997        |
|    value_loss           | 0.0595       |
------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1044         |
|    iterations           | 3            |
|    time_elapsed         | 5            |
|    total_timesteps      | 6144         |
| train/                  |              |
|    approx_kl            | 0.0032421518 |
|    clip_fraction        | 0.00669      |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.83        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0196      |
|    n_updates            | 20           |
|    policy_gradient_loss | -0.000545    |
|    std                  | 0.991        |
|    value_loss           | 0.0351       |
------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1040         |
|    iterations           | 4            |
|    time_elapsed         | 7            |
|    total_timesteps      | 8192         |
| train/                  |              |
|    approx_kl            | 0.0020676744 |
|    clip_fraction        | 0.00283      |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.82        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0212      |
|    n_updates            | 30           |
|    policy_gradient_loss | -0.000439    |
|    std                  | 0.992        |
|    value_loss           | 0.0209       |
------------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1013        |
|    iterations           | 5           |
|    time_elapsed         | 10          |
|    total_timesteps      | 10240       |
| train/                  |             |
|    approx_kl            | 0.004742698 |
|    clip_fraction        | 0.0369      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.82       |
|    explained_variance   | 0.0         |
|    learning_rate        | 0.00025     |
|    loss                 | -0.039      |
|    n_updates            | 40          |
|    policy_gradient_loss | -0.00448    |
|    std                  | 0.985       |
|    value_loss           | 0.0137      |
-----------------------------------------
-------------------------------------------
| time/                   |               |
|    fps                  | 993           |
|    iterations           | 6             |
|    time_elapsed         | 12            |
|    total_timesteps      | 12288         |
| train/                  |               |
|    approx_kl            | 0.0025632828  |
|    clip_fraction        | 0.0113        |
|    clip_range           | 0.2           |
|    entropy_loss         | -2.8          |
|    explained_variance   | 5.9604645e-08 |
|    learning_rate        | 0.00025       |
|    loss                 | -0.0221       |
|    n_updates            | 50            |
|    policy_gradient_loss | -0.000256     |
|    std                  | 0.976         |
|    value_loss           | 0.00675       |
-------------------------------------------
🔍 Sample PPO action: [[1.        0.0499002]]

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ppo Sharpe: nan
ppo Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
a2c Sharpe: nan
a2c Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ddpg Sharpe: nan
ddpg Account Value Range: 1000000.00 to 1000000.00
 Best model: {best_model.__class__.__name__} with Sharpe {best_sharpe:.2f}
❌ No valid model selected — all Sharpe ratios were NaN or invalid.
No results to analyze.
 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 12
  ➤ Train window: 2023-02-04 to 2023-08-04 — 181 days
  ➤ Val window  : 2023-08-04 to 2023-10-04   — 61 days
  ➤ Trade window: 2023-10-04 to 2023-12-04 — 61 days
count    60.000000
mean     -0.000873
std       0.017955
min      -0.073135
25%      -0.004795
50%      -0.001121
75%       0.003691
max       0.060227
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1382 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1091        |
|    iterations           | 2           |
|    time_elapsed         | 3           |
|    total_timesteps      | 4096        |
| train/                  |             |
|    approx_kl            | 0.004411079 |
|    clip_fraction        | 0.0289      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.84       |
|    explained_variance   | 0.62374586  |
|    learning_rate        | 0.00025     |
|    loss                 | 0.00236     |
|    n_updates            | 10          |
|    policy_gradient_loss | -0.0016     |
|    std                  | 0.999       |
|    value_loss           | 0.0781      |
-----------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1034         |
|    iterations           | 3            |
|    time_elapsed         | 5            |
|    total_timesteps      | 6144         |
| train/                  |              |
|    approx_kl            | 0.0066109817 |
|    clip_fraction        | 0.0586       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.84        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.034       |
|    n_updates            | 20           |
|    policy_gradient_loss | -0.00395     |
|    std                  | 1            |
|    value_loss           | 0.0231       |
------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1047         |
|    iterations           | 4            |
|    time_elapsed         | 7            |
|    total_timesteps      | 8192         |
| train/                  |              |
|    approx_kl            | 0.0041546966 |
|    clip_fraction        | 0.0201       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.84        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0243      |
|    n_updates            | 30           |
|    policy_gradient_loss | -0.00122     |
|    std                  | 1            |
|    value_loss           | 0.0139       |
------------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1024        |
|    iterations           | 5           |
|    time_elapsed         | 9           |
|    total_timesteps      | 10240       |
| train/                  |             |
|    approx_kl            | 0.005402865 |
|    clip_fraction        | 0.0366      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.83       |
|    explained_variance   | 0.0         |
|    learning_rate        | 0.00025     |
|    loss                 | -0.047      |
|    n_updates            | 40          |
|    policy_gradient_loss | -0.00452    |
|    std                  | 0.994       |
|    value_loss           | 0.00737     |
-----------------------------------------
----------------------------------------
| time/                   |            |
|    fps                  | 1032       |
|    iterations           | 6          |
|    time_elapsed         | 11         |
|    total_timesteps      | 12288      |
| train/                  |            |
|    approx_kl            | 0.00412568 |
|    clip_fraction        | 0.018      |
|    clip_range           | 0.2        |
|    entropy_loss         | -2.84      |
|    explained_variance   | 0.0        |
|    learning_rate        | 0.00025    |
|    loss                 | -0.0192    |
|    n_updates            | 50         |
|    policy_gradient_loss | -0.00204   |
|    std                  | 1.01       |
|    value_loss           | 0.00412    |
----------------------------------------
🔍 Sample PPO action: [[ 0.8313385  -0.09358758]]

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ppo Sharpe: nan
ppo Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
a2c Sharpe: nan
a2c Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ddpg Sharpe: nan
ddpg Account Value Range: 1000000.00 to 1000000.00
 Best model: {best_model.__class__.__name__} with Sharpe {best_sharpe:.2f}
❌ No valid model selected — all Sharpe ratios were NaN or invalid.
No results to analyze.
 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 13
  ➤ Train window: 2023-05-04 to 2023-11-04 — 184 days
  ➤ Val window  : 2023-11-04 to 2024-01-04   — 61 days
  ➤ Trade window: 2024-01-04 to 2024-03-04 — 60 days
count    60.000000
mean      0.003609
std       0.024043
min      -0.057722
25%      -0.008225
50%       0.002209
75%       0.015539
max       0.063577
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1239 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
-------------------------------------------
| time/                   |               |
|    fps                  | 1118          |
|    iterations           | 2             |
|    time_elapsed         | 3             |
|    total_timesteps      | 4096          |
| train/                  |               |
|    approx_kl            | 0.005141982   |
|    clip_fraction        | 0.0602        |
|    clip_range           | 0.2           |
|    entropy_loss         | -2.85         |
|    explained_variance   | 1.7881393e-07 |
|    learning_rate        | 0.00025       |
|    loss                 | -0.0268       |
|    n_updates            | 10            |
|    policy_gradient_loss | -0.00366      |
|    std                  | 1.01          |
|    value_loss           | 0.00162       |
-------------------------------------------
-----------------------------------------
| time/                   |             |
|    fps                  | 1091        |
|    iterations           | 3           |
|    time_elapsed         | 5           |
|    total_timesteps      | 6144        |
| train/                  |             |
|    approx_kl            | 0.002189481 |
|    clip_fraction        | 0.0084      |
|    clip_range           | 0.2         |
|    entropy_loss         | -2.86       |
|    explained_variance   | 0.0         |
|    learning_rate        | 0.00025     |
|    loss                 | -0.0274     |
|    n_updates            | 20          |
|    policy_gradient_loss | -0.000174   |
|    std                  | 1.02        |
|    value_loss           | 0.000885    |
-----------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 999          |
|    iterations           | 4            |
|    time_elapsed         | 8            |
|    total_timesteps      | 8192         |
| train/                  |              |
|    approx_kl            | 0.0034694783 |
|    clip_fraction        | 0.0237       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.87        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0312      |
|    n_updates            | 30           |
|    policy_gradient_loss | -0.00178     |
|    std                  | 1.02         |
|    value_loss           | 0.00049      |
------------------------------------------
--------------------------------------------
| time/                   |                |
|    fps                  | 986            |
|    iterations           | 5              |
|    time_elapsed         | 10             |
|    total_timesteps      | 10240          |
| train/                  |                |
|    approx_kl            | 0.005120538    |
|    clip_fraction        | 0.0383         |
|    clip_range           | 0.2            |
|    entropy_loss         | -2.88          |
|    explained_variance   | -1.1920929e-07 |
|    learning_rate        | 0.00025        |
|    loss                 | -0.024         |
|    n_updates            | 40             |
|    policy_gradient_loss | -0.00218       |
|    std                  | 1.02           |
|    value_loss           | 0.000309       |
--------------------------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 976          |
|    iterations           | 6            |
|    time_elapsed         | 12           |
|    total_timesteps      | 12288        |
| train/                  |              |
|    approx_kl            | 0.0057744524 |
|    clip_fraction        | 0.0344       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.88        |
|    explained_variance   | 0.0          |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0271      |
|    n_updates            | 50           |
|    policy_gradient_loss | -0.00241     |
|    std                  | 1.02         |
|    value_loss           | 0.000189     |
------------------------------------------
🔍 Sample PPO action: [[-0.7268446  1.       ]]

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ppo Sharpe: nan
ppo Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
a2c Sharpe: nan
a2c Account Value Range: 1000000.00 to 1000000.00

📊 Sharpe Debug:
  ➤ Mean return: nan
  ➤ Std return : nan
  ➤ Sharpe     : nan
ddpg Sharpe: nan
ddpg Account Value Range: 1000000.00 to 1000000.00
 Best model: {best_model.__class__.__name__} with Sharpe {best_sharpe:.2f}
❌ No valid model selected — all Sharpe ratios were NaN or invalid.
No results to analyze.
 Rolling Window {i+1}: {train_start.date()} to {trade_end.date()}
🧪 Window 14
  ➤ Train window: 2023-08-04 to 2024-02-04 — 184 days
  ➤ Val window  : 2024-02-04 to 2024-04-04   — 60 days
  ➤ Trade window: 2024-04-04 to 2024-06-04 — 61 days
count    59.000000
mean      0.007960
std       0.034234
min      -0.084836
25%      -0.009196
50%       0.007727
75%       0.023476
max       0.096181
Name: close, dtype: float64
Using cpu device
-----------------------------
| time/              |      |
|    fps             | 1361 |
|    iterations      | 1    |
|    time_elapsed    | 1    |
|    total_timesteps | 2048 |
-----------------------------
------------------------------------------
| time/                   |              |
|    fps                  | 1241         |
|    iterations           | 2            |
|    time_elapsed         | 3            |
|    total_timesteps      | 4096         |
| train/                  |              |
|    approx_kl            | 0.0049366606 |
|    clip_fraction        | 0.0417       |
|    clip_range           | 0.2          |
|    entropy_loss         | -2.83        |
|    explained_variance   | 0.6548881    |
|    learning_rate        | 0.00025      |
|    loss                 | -0.0262      |
|    n_updates            | 10           |
|    policy_gradient_loss | -0.00326     |
|    std                  | 0.997        |
|    value_loss           | 0.00558      |
------------------------------------------
