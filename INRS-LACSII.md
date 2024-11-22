# Project name: INRS - Monitoring false claims against politicians

**Project description**: Detecting potential political misinformation threats with Lexical Multi-Dimensional Analysis and large-scale Machine Learning algorithms

**Table of Contents**

- [Week 26 to Week 28 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-26-to-week-28-2024---progress-report)
- [Week 29 to Week 30 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-29-to-week-30-2024---progress-report)
- [Week 31, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-31-2024---progress-report)
- [Week 32, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-32-2024---progress-report)
- [Week 33, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-33-2024---progress-report)
- [Week 34 to Week 35, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-34-to-week-35-2024---progress-report)
- [Week 36 to Week 38, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-36-to-week-38-2024---progress-report)
- [Week 39, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-39-2024---progress-report)
- [Week 40, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-40-2024---progress-report)
- [Week 41, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-41-2024---progress-report)
- [Week 42, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-42-2024---progress-report)
- [Week 43, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-43-2024---progress-report)
- [Week 44, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-44-2024---progress-report)
- [Week 45, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-45-2024---progress-report)
- [Week 46, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-46-2024---progress-report)
- [Week 47, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-47-2024---progress-report)
- [Week 48, 2024 - Progress Report](https://github.com/lacsii/Weekly-report/blob/main/rogerio/rogerio.md#week-48-2024---progress-report)

## Week 26 to Week 28, 2024 - Progress Report

In response to my action point, a [US Presidential and Vice Presidential debates](https://www.debates.org/voter-education/debate-transcripts/) _corpus_ was compiled via web scraping. 

- Repository: https://github.com/laelgelc/cl_st1_inrs;
- _Corpus_ design solution description: https://github.com/laelgelc/cl_st1_inrs/blob/main/CL_St1_Ph1_INRS.ipynb;
- _Corpus_: https://github.com/laelgelc/cl_st1_inrs/tree/main/cl_st1_inrs.

The _corpus_ consists of all of the 47 debates and is ready for Lexical Multidimensional Analysis. Claudia and I met on Week 27 to validate the data format.

## Week 29 to Week 30, 2024 - Progress Report

Professor Tony, Claudia and I met on 16/07/2024 and defined the way forward of the Lexical Multidimensional Analysis as:

- Target _corpus_ definition:
  - Definition of text: In this study, a text is defined as a turn of a candidate consisting of at least 10 words. Therefore, the speeches of the moderators and members of the audience should not be considered;
- The goal of the Lexical Multidimensional Analysis is to detemine the dimensional profile of the debates.

Target _corpus_ deliverables:
- Target _corpus_ design solution description: https://github.com/laelgelc/cl_st1_inrs/blob/main/CL_St1_Ph2_INRS.ipynb;
- Target _corpus_: https://github.com/laelgelc/cl_st1_inrs/tree/main/cl_st1_inrs_tc.

The target _corpus_ consists of 3,217 texts.

On 23/07/2024, Professor Tony shared information about [research design and question generation](https://www.dropbox.com/scl/fo/f8arh0sc7vmlqmraprm1g/ANBUZxbSj0-psw3Rbls0hWM?rlkey=6mtalecd4p6gy9rroysevbj3q&dl=0) agreed with Professor Anderson that day.

### Meeting on 24/07/2024

In response to my action point, the target _corpus_ has been split according the political parties of the participants:

- Republican: 1,837 texts;
- Democratic: 1,534 texts;
- independent: 107 texts.

To that end, the solution [CL_St1_Ph2_INRS.ipynb](https://github.com/laelgelc/cl_st1_inrs/blob/main/CL_St1_Ph2_INRS.ipynb) was extended with the section 'Splitting the target corpus according to the political party of the participants'. In the process of developing the solution, a few corrections were implemented allowing us to harvest a few new turns (texts) - from 3,217 to 3,478 texts.

An inconsistency has been identified in the section 'Grouping paragraphs into turns' that incorrectly assigns the metadata of the next debate to the last speaker of the previous debate in case he or she had paragraphs grouped in a turn. This should not be a blocking issue to the project at the moment since the experiments with RAG are focusing on the column 'Text' of the data sets. Anyway, a fix should be provided and you should be informed. This issue has been fixed in commit [20240725-1916](https://github.com/laelgelc/cl_st1_inrs/commit/cfff7fdb2c839ee8d366402ca1353ffc3634064f).

Please redownload the target _corpus_:
- Target _corpus_: https://github.com/laelgelc/cl_st1_inrs/tree/main/cl_st1_inrs_tc

The new parts are provided in both JSONL and TSV formats. Note that the original dataset that contains all texts remains available:

```
(my_env) eyamrog@Rog-ASUS:~/work/cl_st1_inrs/cl_st1_inrs_tc$ ll
total 16232
drwxr-xr-x 2 eyamrog eyamrog    4096 Aug  1 13:26 ./
drwxr-xr-x 8 eyamrog eyamrog    4096 Oct  5 09:42 ../
-rw-r--r-- 1 eyamrog eyamrog 4271362 Aug  1 13:26 debates_turns.jsonl
-rw-r--r-- 1 eyamrog eyamrog 3893618 Aug  1 13:26 debates_turns.tsv
-rw-r--r-- 1 eyamrog eyamrog 2008078 Aug  1 13:26 debates_turns_democratic.jsonl
-rw-r--r-- 1 eyamrog eyamrog 1841016 Aug  1 13:26 debates_turns_democratic.tsv
-rw-r--r-- 1 eyamrog eyamrog  145148 Aug  1 13:26 debates_turns_independent.jsonl
-rw-r--r-- 1 eyamrog eyamrog  132903 Aug  1 13:26 debates_turns_independent.tsv
-rw-r--r-- 1 eyamrog eyamrog 2118136 Aug  1 13:26 debates_turns_republican.jsonl
-rw-r--r-- 1 eyamrog eyamrog 1919809 Aug  1 13:26 debates_turns_republican.tsv
-rw-r--r-- 1 eyamrog eyamrog  264640 Aug  1 13:26 unique_words.txt
(my_env) eyamrog@Rog-ASUS:~/work/cl_st1_inrs/cl_st1_inrs_tc$ 
```

## Week 31, 2024 - Progress Report
Professors Tony and Claudia and I have been examining the preliminary dimensional profile of the target _corpus_ considering:
- `Republican + Democratic + Independent` target _corpus_;
- `Republican + Independent` target _corpus_ subset;
- `Democratic + Independent` target _corpus_ subset.

### Meeting on 31/07/2024
Cláudia analysed the set of questions to be made to the LLMs and we revised them. It has been decided to have them refined in order to make them more specific and less subject to ambiguity.

## Week 32, 2024 - Progress Report
Professors Tony, Claudia, Paula Pinto and Marcos and I met on 13/08/2024 to evaluate the status of the linguistic side of the experiments.

### Meeting on 14/08/2024
The team discussed the progress on the linguistic side of the experiments. Among other aspects, Professor Tony emphasised the distinction between information (or topics) and discourses. The methods of the experiments with RAG tend to consider the External Knowledge corpus as source of information expected to influence the behaviour of the LLM. The experiments are designed to evaluate, for instance, how much influenced towards the Democratic ideology the RAG system would become if presented with an External Knowledge consisting of texts from Democratic presidential candidates. However, firstly, it is known that even though the Republican and Democratic parties may manifest opposing positions about a specific topic (especially in a context of political contest), their ideologies present significant overlap (if anything, both are Right-Wing parties). Secondly, discourses run below the surface of apparent information/topics - they are detectable by the systematic use of linguistic features but they operate regardless of the apparent consistence of a certain piece of information or particular opinion about a topic. Professor Tony explained that the texts to build the External Knowledge logic could be enriched with dimensional information (a set of scores of each text towards each dimension) in an attempt to raise the External Knowledge logic's awareness of the dimensions that define the underlying discourses. He added that an LMDA on the output of the LLM may reveal how much its response became aligned with the dimensional profile of the corpus provided to the External Knowledge.

## Week 33, 2024 - Progress Report
We received guidance from Professor Tony on the way forward of the LMDAs:
- The LMDAs should employ key words instead of top lemmas. Professor Tony indicated as reference the study of GELC's Group 5, specifically the artefacts in the folder `1`;
- The entire corpus (`Republican + Democratic + Independent`) should be considered for the LMDA;
- The `stoplist` should be properly build in order to exclude lemmas that are of no consequence (proper nouns, prepositions, verb forms, etc.) to the analysis;
- Professor Tony also recommended that the key-word list should also be critically inspected.

In response to the need to gain access to the scholarship grant from INRS, a small-scale business was started as Individual Microentrepreneur accoding to the Brazilian law ([MEI](https://www.gov.br/empresas-e-negocios/pt-br/empreendedor)).

## Week 34 to Week 35, 2024 - Progress Report
Attempts to reproduce the processing of the study of GELC's Group 5 were conducted with partial success. It was possible to execute the Bash script functions `splitfiles` and `refcleanup` with adaptations from macOS to Linux Ubuntu. When executing `pseudocleanup`, however, it has been discovered that the contents of the directory `corpus/pseudo_temp` were missing.

```
(my_env) eyamrog@Rog-ASUS:~/work/scratchpad$ bash group_5_v2.sh*
find: ‘corpus/pseudo_temp’: No such file or directory
find: ‘corpus/pseudo_temp’: No such file or directory
find: ‘corpus/pseudo’: No such file or directory
(my_env) eyamrog@Rog-ASUS:~/work/scratchpad$ 
```

Professor Tony should be consulted about this piece of missing information before work is resumed.

On 04/09/2024, an alternative to extract the key words via the Python package `YAKE!` has been tentatively executed, apparently with good results. The Proof-of-Concept of this solution and the final solution can be found here:
- `YAKE!` PoC: https://github.com/laelgelc/cl_st1_inrs/blob/main/CL_St1_PoC1_INRS.ipynb;
- LMDA solution with key word extraction via `YAKE!`: https://github.com/laelgelc/cl_st1_inrs/blob/main/CL_St1_Ph4_INRS.ipynb.

On 05/09/2024, the results of the LMDA processing according to the mentioned requirements became available. They were circulated to the Corpus Linguistics Team for further analysis and interpretation.

## Week 36 to Week 38, 2024 - Progress Report
Nothing to report.

## Week 39, 2024 - Progress Report
### Meeting on 23/09/2024
In this meeting, Professor Anderson, Cláudia, Hazem and I agreed upon the following action points:
- Compile the 50 most representative texts of Dimension 1 and provide them to Hazem. Resp.: Cláudia. Due: this week;
- Compile the corresponding questions and provide them to Hazem. Resp.: Cláudia. Due: this week;
- Provide Cláudia with the [raw data set containing the transcripts of all of the debates](https://github.com/laelgelc/cl_st1_inrs/blob/main/CL_St1_Ph1_INRS.tar.gz) in order to facilitate the retrieval of the questions. Resp.: Rogério. Due: done;
- Prepare the External Knowledge database with the texts. Resp.: Hazem. Due: this week;
- Use the questions to run two test scenarios - with RAG and withour RAG - and provide the results to the Corpus Linguistics Team. Resp.: Hazem. Due: ongoing;
- Perform an ANOVA (Analysis of Variance) to determine if the differences observed between Republicans and Democrats are due to actual differences or just random chance. Resp.: Corpus Linguistics Team. Due: ongoing

## Week 40, 2024 - Progress Report
### Meeting on 30/09/2024
In this meeting Cláudia and I met Carlos Kauffmann and Rafael Fonseca and learned how to run `One-Way ANOVA` in `SAS OnDemand for Academics`:
- Enrich the file `cl_st1_ph4_inrs_scores_only.tsv` to include a column `Party` with categories `r` for `Republican` and `d` for `Democratic`, for instance;
- Run `One-Way ANOVA` for each dimension using the `Party` as the categorical variable;
- Rafael suggested that a column `Decade` is included;
- The group agreed to meet again in two weeks' time.

In response to the plan, the following actions have been completed:
- The columns `Decade` and `Party` were added to the target _corpus_, `debates_turns.jsonl`;
- The updated target _corpus_ was enriched with the factor scores reported in the document `cl_st1_ph4_inrs_scores_only.tsv` and the resulting document was named `debates_turns_parties_scores.tsv`;
- `debates_turns_parties_scores.tsv` was processed in SAS OnDemand for Academics using the linear model One-Way ANOVA;
- The results were made available in [cl_st1_inrs_anova](https://github.com/laelgelc/cl_st1_inrs/tree/main/cl_st1_inrs_anova).

## Week 41, 2024 - Progress Report
The Corpus Linguistics Team is engaged in interpreting the factors of the Lexical Multi-Dimensional Analysis having ChatGPT as an analysis assistant. The following data set was prepared for the task:
- [cl_st1_inrs_interpretation](https://github.com/laelgelc/cl_st1_inrs/tree/main/cl_st1_inrs_interpretation).

ANOVA having a new column `Election` as categorical variable have been commissioned:
- The results were made available in [cl_st1_inrs_anova](https://github.com/laelgelc/cl_st1_inrs/tree/main/cl_st1_inrs_anova).

## Week 42, 2024 - Progress Report
The texts were exported to individual text files for inspection: [sas_exercise](https://github.com/laelgelc/cl_st1_inrs/tree/main/cl_st1_inrs_anova/sas_exercise).

## Week 43, 2024 - Progress Report
On 24/10/2024 Professor Tony commented that when calculating ANOVA, we should exclude texts whose score is 0. Therefore, we will recalculate ANOVA according to this direction.

## Week 44, 2024 - Progress Report
In response to the action point taken last week, ANOVA having a new column `Election` as categorical variable and excluding texts whose score was 0 have been commissioned:
- The results were made available in [cl_st1_inrs_anova](https://github.com/laelgelc/cl_st1_inrs/tree/main/cl_st1_inrs_anova).

## Week 45, 2024 - Progress Report
In the meeting on 08/11/2024, Claudia reported that, on the US Presidential Debates side, there could not be found much difference in the discourses between Republican and Democratic candidates. The expectation of finding opposing/polarised discourses could not be confirmed. In the face of these findings, she suggested the use of the dimensions as a guide to opposing stances. She explained that she, aligned with Professor Tony, has been prompting ChatGPT 4.0 to generate knowledge that opposes the ideologies uncovered by the Multi-Dimensional Analysis. Professor Anderson argued that this could be used to create the opposing external knowledge we failed to obtain from the analysis of the Presidential Debates Corpus.

Professor Anderson said that ChatGPT 3.5 does not use RAG - 4.0 does (it is not naïve), but we have no control over the external knowledge it uses.

Therefore, our target now is to compile an opposing external knowledge by prompting ChatGPT to create texts that express opposite ideologies. There are 50 top scoring texts in each of the 6 dimensions, which makes up 300 queries to ChatGPT. I suggested that we used the ChatGPT API for the job.

We might need to do the same with the Pseudo-Science (COVID-19) corpus.

## Week 46, 2024 - Progress Report
In response to the action point:
- A solution to automate queries to ChatGPT for processing the top-score texts in each dimension was developed: [CL_St1_Ph5_INRS.ipynb](https://github.com/laelgelc/cl_st1_inrs/blob/main/CL_St1_Ph5_INRS.ipynb);
- A full compilation of the turns of the debates in Excel format was prepared: [debates_turns_raw.xlsx](https://github.com/laelgelc/cl_st1_inrs/blob/main/cl_st1_inrs_tc/debates_turns_raw.xlsx).

## Week 47, 2024 - Progress Report
The solution was adapted to process `Host Questions`:
- Solution: https://github.com/laelgelc/cl_st1_inrs/blob/main/CL_St1_Ph6_INRS.ipynb;
- A Proof of Concept with `Dimension 1 - Positive Pole` was processed.

After reviewing the results of the Proof of Concept with Claudia. we decided to use the solution to process `Dimension 6 - Positive and Negative Poles`:
- The results were made available in [cl_st1_ph6_inrs](https://github.com/laelgelc/cl_st1_inrs/tree/main/cl_st1_ph6_inrs).

## Week 48, 2024 - Progress Report
Arrangements for a Lexical Multi-Dimensional Analysis workshop planned for week 50.
