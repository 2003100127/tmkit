# Versions


## {octicon}`share;1em;sd-text-info` **Release**

| version | time       | who          | status   | note |
|---------|------------|--------------|----------|------|
| v0.0.1  | 05.03.2023 | Jianfeng Sun | success  |      |
| v0.0.2  | 18.06.2023 | Jianfeng Sun | success  |      |
| v0.0.3  | 06.07.2023 | Jianfeng Sun | success  |      |



## {octicon}`shield-check;1em;sd-text-info` **Change logs**
...


## {octicon}`report;1em;sd-text-info` **Test reports**

```{article-info}
:avatar: ./img/jsun.ico
:avatar-link: https://scholar.google.com/citations?hl=en&user=TfLBR9kAAAAJ&view_op=list_works&sortby=pubdate
:avatar-outline: muted
:author: Jianfeng Sun
:date: **July 6, 2023**
:read-time: 10 min
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```


{octicon}`check-circle-fill;1em;sd-text-success`**Test 1**

::::{tab-set}

:::{tab-item} {octicon}`tools;1em;sd-text-info`**system parameters**
* {bdg-dark-line}`Python` 3.11.4 
* {bdg-dark-line}`conda` 4.12.0 
* {bdg-dark-line}`install` Github (also PyPI)
* {bdg-dark-line}`system` Windows10 (also Ubuntu 20.04)
:::

:::{tab-item} {octicon}`log;1em;sd-text-info`**test logs**
```{code} shell
(tmkit) D:\Document\Programming\Python\deepbio\symphony\github\tmkit>pip install .
Processing d:\document\programming\python\deepbio\symphony\github\tmkit
  Preparing metadata (setup.py) ... done
Collecting scikit-learn (from tmkit==0.0.0.2)
  Downloading scikit_learn-1.3.0-cp311-cp311-win_amd64.whl (9.2 MB)
     ---------------------------------------- 9.2/9.2 MB 2.9 MB/s eta 0:00:00
Collecting pandas (from tmkit==0.0.0.2)
  Downloading pandas-2.0.3-cp311-cp311-win_amd64.whl (10.6 MB)
     ---------------------------------------- 10.6/10.6 MB 6.3 MB/s eta 0:00:00
Collecting numpy (from tmkit==0.0.0.2)
  Using cached numpy-1.25.0-cp311-cp311-win_amd64.whl (15.0 MB)
Collecting openpyxl (from tmkit==0.0.0.2)
  Using cached openpyxl-3.1.2-py2.py3-none-any.whl (249 kB)
Collecting biopandas (from tmkit==0.0.0.2)
  Using cached biopandas-0.4.1-py2.py3-none-any.whl (878 kB)
Collecting pypdb==2.2 (from tmkit==0.0.0.2)
  Using cached pypdb-2.2-py3-none-any.whl (34 kB)
Collecting xmltramp2==3.1.1 (from tmkit==0.0.0.2)
  Using cached xmltramp2-3.1.1-py3-none-any.whl
Collecting biopython==1.79 (from tmkit==0.0.0.2)
  Using cached biopython-1.79-cp311-cp311-win_amd64.whl (2.3 MB)
Collecting pyfiglet==0.8.post1 (from tmkit==0.0.0.2)
  Using cached pyfiglet-0.8.post1-py2.py3-none-any.whl (865 kB)
Collecting requests (from pypdb==2.2->tmkit==0.0.0.2)
  Using cached requests-2.31.0-py3-none-any.whl (62 kB)
Collecting six (from xmltramp2==3.1.1->tmkit==0.0.0.2)
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: setuptools in d:\programming\anaconda3\envs\tmkit\lib\site-packages (from biopandas->tmkit==0.0.0.2) (68.0.0)
Collecting python-dateutil>=2.8.2 (from pandas->tmkit==0.0.0.2)
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting pytz>=2020.1 (from pandas->tmkit==0.0.0.2)
  Using cached pytz-2023.3-py2.py3-none-any.whl (502 kB)
Collecting tzdata>=2022.1 (from pandas->tmkit==0.0.0.2)
  Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
Collecting et-xmlfile (from openpyxl->tmkit==0.0.0.2)
  Using cached et_xmlfile-1.1.0-py3-none-any.whl (4.7 kB)
Collecting scipy>=1.5.0 (from scikit-learn->tmkit==0.0.0.2)
  Downloading scipy-1.11.1-cp311-cp311-win_amd64.whl (44.0 MB)
     ---------------------------------------- 44.0/44.0 MB 7.4 MB/s eta 0:00:00
Collecting joblib>=1.1.1 (from scikit-learn->tmkit==0.0.0.2)
  Downloading joblib-1.3.1-py3-none-any.whl (301 kB)
     ---------------------------------------- 302.0/302.0 kB 1.0 MB/s eta 0:00:00
Collecting threadpoolctl>=2.0.0 (from scikit-learn->tmkit==0.0.0.2)
  Using cached threadpoolctl-3.1.0-py3-none-any.whl (14 kB)
Collecting charset-normalizer<4,>=2 (from requests->pypdb==2.2->tmkit==0.0.0.2)
  Using cached charset_normalizer-3.1.0-cp311-cp311-win_amd64.whl (96 kB)
Collecting idna<4,>=2.5 (from requests->pypdb==2.2->tmkit==0.0.0.2)
  Using cached idna-3.4-py3-none-any.whl (61 kB)
Collecting urllib3<3,>=1.21.1 (from requests->pypdb==2.2->tmkit==0.0.0.2)
  Using cached urllib3-2.0.3-py3-none-any.whl (123 kB)
Collecting certifi>=2017.4.17 (from requests->pypdb==2.2->tmkit==0.0.0.2)
  Using cached certifi-2023.5.7-py3-none-any.whl (156 kB)
Building wheels for collected packages: tmkit
  Building wheel for tmkit (setup.py) ... done
  Created wheel for tmkit: filename=tmkit-0.0.0.2-py3-none-any.whl size=126845 sha256=d0c281f14de1a88d5f6ab4823beef5bf5ab2c76b2a9d192b115f7eda96a81673
  Stored in directory: C:\Users\jianf\AppData\Local\Temp\pip-ephem-wheel-cache-w38g_yjh\wheels\82\82\23\5336955fb4e65eecd46be3d7456ca520d46b96168443a78564
Successfully built tmkit
Installing collected packages: pytz, pyfiglet, urllib3, tzdata, threadpoolctl, six, numpy, joblib, idna, et-xmlfile, charset-normalizer, certifi, xmltramp2, scipy, requests, python-dateutil, openpyxl, biopython, scikit-learn, pypdb, pandas, biopandas, tmkit
Successfully installed biopandas-0.4.1 biopython-1.79 certifi-2023.5.7 charset-normalizer-3.1.0 et-xmlfile-1.1.0 idna-3.4 joblib-1.3.1 numpy-1.25.0 openpyxl-3.1.2 pandas-2.0.3
pyfiglet-0.8.post1 pypdb-2.2 python-dateutil-2.8.2 pytz-2023.3 requests-2.31.0 scikit-learn-1.3.0 scipy-1.11.1 six-1.16.0 threadpoolctl-3.1.0 tmkit-0.0.0.2 tzdata-2023.3 urllib3-2.0.3 xmltramp2-3.1.1
```
:::

::::


{octicon}`check-circle-fill;1em;sd-text-success`**Test 2**

::::{tab-set}

:::{tab-item} {octicon}`tools;1em;sd-text-info`**system parameters**
* {bdg-dark-line}`Python` 3.10.12
* {bdg-dark-line}`conda` 4.12.0 
* {bdg-dark-line}`install` Github (also PyPI)
* {bdg-dark-line}`system` Windows10
:::

:::{tab-item} {octicon}`log;1em;sd-text-info`**test logs**
```{code} shell
(tmkit1) C:\Users\jianf>pip install tmkit==0.0.2
Collecting tmkit==0.0.2
  Using cached tmkit-0.0.2.tar.gz (90 kB)
  Preparing metadata (setup.py) ... done
Collecting scikit-learn (from tmkit==0.0.2)
  Downloading scikit_learn-1.3.0-cp310-cp310-win_amd64.whl (9.2 MB)
     ---------------------------------------- 9.2/9.2 MB 5.5 MB/s eta 0:00:00
Collecting pandas (from tmkit==0.0.2)
  Downloading pandas-2.0.3-cp310-cp310-win_amd64.whl (10.7 MB)
     ---------------------------------------- 10.7/10.7 MB 5.9 MB/s eta 0:00:00
Collecting numpy (from tmkit==0.0.2)
  Downloading numpy-1.25.0-cp310-cp310-win_amd64.whl (15.0 MB)
     ---------------------------------------- 15.0/15.0 MB 13.1 MB/s eta 0:00:00
Collecting openpyxl (from tmkit==0.0.2)
  Using cached openpyxl-3.1.2-py2.py3-none-any.whl (249 kB)
Collecting biopandas (from tmkit==0.0.2)
  Using cached biopandas-0.4.1-py2.py3-none-any.whl (878 kB)
Collecting pypdb==2.2 (from tmkit==0.0.2)
  Using cached pypdb-2.2-py3-none-any.whl (34 kB)
Collecting xmltramp2==3.1.1 (from tmkit==0.0.2)
  Using cached xmltramp2-3.1.1.tar.gz (6.7 kB)
  Preparing metadata (setup.py) ... done
Collecting biopython==1.79 (from tmkit==0.0.2)
  Downloading biopython-1.79-cp310-cp310-win_amd64.whl (2.3 MB)
     ---------------------------------------- 2.3/2.3 MB 3.4 MB/s eta 0:00:00
Collecting pyfiglet==0.8.post1 (from tmkit==0.0.2)
  Using cached pyfiglet-0.8.post1-py2.py3-none-any.whl (865 kB)
Collecting requests (from pypdb==2.2->tmkit==0.0.2)
  Using cached requests-2.31.0-py3-none-any.whl (62 kB)
Collecting six (from xmltramp2==3.1.1->tmkit==0.0.2)
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: setuptools in d:\programming\anaconda3\envs\tmkit1\lib\site-packages (from biopandas->tmkit==0.0.2) (68.0.0)
Collecting python-dateutil>=2.8.2 (from pandas->tmkit==0.0.2)
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting pytz>=2020.1 (from pandas->tmkit==0.0.2)
  Using cached pytz-2023.3-py2.py3-none-any.whl (502 kB)
Collecting tzdata>=2022.1 (from pandas->tmkit==0.0.2)
  Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
Collecting et-xmlfile (from openpyxl->tmkit==0.0.2)
  Using cached et_xmlfile-1.1.0-py3-none-any.whl (4.7 kB)
Collecting scipy>=1.5.0 (from scikit-learn->tmkit==0.0.2)
  Downloading scipy-1.11.1-cp310-cp310-win_amd64.whl (44.0 MB)
     ---------------------------------------- 44.0/44.0 MB 8.8 MB/s eta 0:00:00
Collecting joblib>=1.1.1 (from scikit-learn->tmkit==0.0.2)
  Using cached joblib-1.3.1-py3-none-any.whl (301 kB)
Collecting threadpoolctl>=2.0.0 (from scikit-learn->tmkit==0.0.2)
  Using cached threadpoolctl-3.1.0-py3-none-any.whl (14 kB)
Collecting charset-normalizer<4,>=2 (from requests->pypdb==2.2->tmkit==0.0.2)
  Downloading charset_normalizer-3.1.0-cp310-cp310-win_amd64.whl (97 kB)
     ---------------------------------------- 97.1/97.1 kB 5.8 MB/s eta 0:00:00
Collecting idna<4,>=2.5 (from requests->pypdb==2.2->tmkit==0.0.2)
  Using cached idna-3.4-py3-none-any.whl (61 kB)
Collecting urllib3<3,>=1.21.1 (from requests->pypdb==2.2->tmkit==0.0.2)
  Using cached urllib3-2.0.3-py3-none-any.whl (123 kB)
Collecting certifi>=2017.4.17 (from requests->pypdb==2.2->tmkit==0.0.2)
  Using cached certifi-2023.5.7-py3-none-any.whl (156 kB)
Building wheels for collected packages: tmkit, xmltramp2
  Building wheel for tmkit (setup.py) ... done
  Created wheel for tmkit: filename=tmkit-0.0.2-py3-none-any.whl size=126820 sha256=8b9a3aea025c331054bfbb1ea2bd85ed93e57720648bc53a0f0e4f500677117d
  Stored in directory: c:\users\jianf\appdata\local\pip\cache\wheels\ee\58\12\af9f861f381f0a053abcc1dafb852d8c4509d705155f87dd3b
  Building wheel for xmltramp2 (setup.py) ... done
  Created wheel for xmltramp2: filename=xmltramp2-3.1.1-py3-none-any.whl size=7342 sha256=aebbc8dfc223fc198e6d66a3ccb6a71f1bcdd076079bea32bc894f937586267c
  Stored in directory: c:\users\jianf\appdata\local\pip\cache\wheels\c0\ce\4f\44f18aefe657d47acbcbcafe21743b4fed1bfd6c9fd0e85ab2
Successfully built tmkit xmltramp2
Installing collected packages: pytz, pyfiglet, urllib3, tzdata, threadpoolctl, six, numpy, joblib, idna, et-xmlfile, charset-normalizer, certifi, xmltramp2, scipy, requests, python-dateutil, openpyxl, biopython, scikit-learn, pypdb, pandas, biopandas, tmkit
Successfully installed biopandas-0.4.1 biopython-1.79 certifi-2023.5.7 charset-normalizer-3.1.0 et-xmlfile-1.1.0 idna-3.4 joblib-1.3.1 numpy-1.25.0 openpyxl-3.1.2 pandas-2.0.3
pyfiglet-0.8.post1 pypdb-2.2 python-dateutil-2.8.2 pytz-2023.3 requests-2.31.0 scikit-learn-1.3.0 scipy-1.11.1 six-1.16.0 threadpoolctl-3.1.0 tmkit-0.0.2 tzdata-2023.3 urllib3-2.0.3 xmltramp2-3.1.1
```
:::

::::




{octicon}`check-circle-fill;1em;sd-text-success`**Test 3**

::::{tab-set}

:::{tab-item} {octicon}`tools;1em;sd-text-info`**system parameters**
* {bdg-dark-line}`Python` 3.9.17
* {bdg-dark-line}`conda` 4.11.0
* {bdg-dark-line}`install` Github (also PyPI)
* {bdg-dark-line}`system` Ubuntu 20.04
:::

:::{tab-item} {octicon}`log;1em;sd-text-info`**test logs**
```{code} shell
(tmkit) jsun@DESKTOP-68LV7AB:~$ pip install tmkit==0.0.2
Collecting tmkit==0.0.2
  Using cached tmkit-0.0.2.tar.gz (90 kB)
  Preparing metadata (setup.py) ... done
Collecting scikit-learn (from tmkit==0.0.2)
  Downloading scikit_learn-1.3.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (10.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.9/10.9 MB 6.0 MB/s eta 0:00:00
Collecting pandas (from tmkit==0.0.2)
  Downloading pandas-2.0.3-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.4/12.4 MB 6.1 MB/s eta 0:00:00
Collecting numpy (from tmkit==0.0.2)
  Downloading numpy-1.25.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.7/17.7 MB 15.6 MB/s eta 0:00:00
Collecting openpyxl (from tmkit==0.0.2)
  Downloading openpyxl-3.1.2-py2.py3-none-any.whl (249 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 250.0/250.0 kB 12.0 MB/s eta 0:00:00
Collecting biopandas (from tmkit==0.0.2)
  Downloading biopandas-0.4.1-py2.py3-none-any.whl (878 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 879.0/879.0 kB 9.1 MB/s eta 0:00:00
Collecting pypdb==2.2 (from tmkit==0.0.2)
  Downloading pypdb-2.2-py3-none-any.whl (34 kB)
Collecting xmltramp2==3.1.1 (from tmkit==0.0.2)
  Downloading xmltramp2-3.1.1.tar.gz (6.7 kB)
  Preparing metadata (setup.py) ... done
Collecting biopython==1.79 (from tmkit==0.0.2)
  Downloading biopython-1.79-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.7/2.7 MB 6.5 MB/s eta 0:00:00
Collecting pyfiglet==0.8.post1 (from tmkit==0.0.2)
  Using cached pyfiglet-0.8.post1-py2.py3-none-any.whl (865 kB)
Collecting requests (from pypdb==2.2->tmkit==0.0.2)
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6 kB 2.7 MB/s eta 0:00:00
Collecting six (from xmltramp2==3.1.1->tmkit==0.0.2)
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: setuptools in ./anaconda3/envs/tmkit/lib/python3.9/site-packages (from biopandas->tmkit==0.0.2) (67.8.0)
Collecting python-dateutil>=2.8.2 (from pandas->tmkit==0.0.2)
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting pytz>=2020.1 (from pandas->tmkit==0.0.2)
  Using cached pytz-2023.3-py2.py3-none-any.whl (502 kB)
Collecting tzdata>=2022.1 (from pandas->tmkit==0.0.2)
  Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
Collecting et-xmlfile (from openpyxl->tmkit==0.0.2)
  Downloading et_xmlfile-1.1.0-py3-none-any.whl (4.7 kB)
Collecting scipy>=1.5.0 (from scikit-learn->tmkit==0.0.2)
  Downloading scipy-1.11.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (36.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 36.5/36.5 MB 13.5 MB/s eta 0:00:00
Collecting joblib>=1.1.1 (from scikit-learn->tmkit==0.0.2)
  Downloading joblib-1.3.1-py3-none-any.whl (301 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 302.0/302.0 kB 23.3 MB/s eta 0:00:00
Collecting threadpoolctl>=2.0.0 (from scikit-learn->tmkit==0.0.2)
  Using cached threadpoolctl-3.1.0-py3-none-any.whl (14 kB)
Collecting charset-normalizer<4,>=2 (from requests->pypdb==2.2->tmkit==0.0.2)
  Downloading charset_normalizer-3.1.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (199 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 199.2/199.2 kB 19.0 MB/s eta 0:00:00
Collecting idna<4,>=2.5 (from requests->pypdb==2.2->tmkit==0.0.2)
  Downloading idna-3.4-py3-none-any.whl (61 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.5/61.5 kB 6.3 MB/s eta 0:00:00
Collecting urllib3<3,>=1.21.1 (from requests->pypdb==2.2->tmkit==0.0.2)
  Downloading urllib3-2.0.3-py3-none-any.whl (123 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 123.6/123.6 kB 5.6 MB/s eta 0:00:00
Collecting certifi>=2017.4.17 (from requests->pypdb==2.2->tmkit==0.0.2)
  Downloading certifi-2023.5.7-py3-none-any.whl (156 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 157.0/157.0 kB 5.4 MB/s eta 0:00:00
Building wheels for collected packages: tmkit, xmltramp2
  Building wheel for tmkit (setup.py) ... done
  Created wheel for tmkit: filename=tmkit-0.0.2-py3-none-any.whl size=126814 sha256=4ee0217af2e4410c90d04c99139093b4d04ac81877ef39657483407b94c1c4b2
  Stored in directory: /home/jsun/.cache/pip/wheels/87/4c/f0/775490eb43a4ab0b4414c9da46181d47eb4b9e0c85b7dfbd9c
  Building wheel for xmltramp2 (setup.py) ... done
  Created wheel for xmltramp2: filename=xmltramp2-3.1.1-py3-none-any.whl size=7314 sha256=2ded5ec37f707af6ef7fdd877cadbfb3db78f42f388bf21c61f7d8f180c7321c
  Stored in directory: /home/jsun/.cache/pip/wheels/f5/62/42/3499542889072e2014b670c46f963313862c86adc55229d2d5
  Successfully built tmkit xmltramp2
Installing collected packages: pytz, pyfiglet, urllib3, tzdata, threadpoolctl, six, numpy, joblib, idna, et-xmlfile, charset-normalizer, certifi, xmltramp2, scipy, requests, python-dateutil, openpyxl, biopython, scikit-learn, pypdb, pandas, biopandas, tmkit
Successfully installed biopandas-0.4.1 biopython-1.79 certifi-2023.5.7 charset-normalizer-3.1.0 et-xmlfile-1.1.0 idna-3.4 joblib-1.3.1 numpy-1.25.0 openpyxl-3.1.2 pandas-2.0.3 pyfiglet-0.8.post1 pypdb-2.2 python-dateutil-2.8.2 pytz-2023.3 requests-2.31.0 scikit-learn-1.3.0 scipy-1.11.1 six-1.16.0 threadpoolctl-3.1.0 tmkit-0.0.2 tzdata-2023.3 urllib3-2.0.3 xmltramp2-3.1.1
```
:::

::::
