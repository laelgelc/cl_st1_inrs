# Corpus Linguistics - Study 1 - Phase 3 - INRS

## Prerequisites

#Make sure the prerequisites in [CL_LMDA_prerequisites](https://github.com/laelgelc/laelgelc/blob/main/CL_LMDA_prerequisites.ipynb) are satisfied.

## Dataset

#Please download the following dataset (Right-click on the link and choose `Save link as` to download the corresponding file):
#- [CL_St1_Ph2_INRS.tar.gz](https://github.com/laelgelc/cl_st1_inrs/blob/main/CL_St1_Ph2_INRS.tar.gz)

## Importing the required libraries

import pandas as pd
import demoji
import re
import os
from collections import Counter

## Data wrangling

### Importing the tweet raw data into a dataframe

df_tweets_raw_data = pd.read_csv('cl_st1_inrs_tc/debates_turns.tsv', sep='\t')

df_tweets_raw_data.dtypes

df_tweets_raw_data['Date'] = pd.to_datetime(df_tweets_raw_data['Date'])
#df_tweets_raw_data['Date'] = df_tweets_raw_data['Date'].astype('datetime64[ns]') # Alternative command

df_tweets_raw_data.dtypes

df_tweets_raw_data.head(5)

df_tweets_raw_data.shape

#### Inspecting a few tweets

inspected_row = 0
print('Speaker:' + df_tweets_raw_data.loc[inspected_row, 'Speaker'])
print('Text:' + df_tweets_raw_data.loc[inspected_row, 'Text'])

## Sampling the raw data according to filtering expressions

# Bypassing the screening by filtering expressions because it is not relevant in this case
df_tweets_filtered = df_tweets_raw_data

df_tweets_filtered

### Exporting the filtered data into a file for inspection

df_tweets_filtered.to_csv('tweets_emojified.tsv', sep='\t', index=False)

df_tweets_filtered.to_json('tweets_emojified.jsonl', orient='records', lines=True)

## Replacing emojis

### Demojifying the column `text`

# Defining a function to demojify a string
def demojify_line(input_line):
    demojified_line = demoji.replace_with_desc(input_line, sep='<em>')
    return demojified_line

df_tweets_filtered['Text'] = df_tweets_filtered['Text'].apply(demojify_line)

#### Exporting the filtered data into a file for inspection

df_tweets_filtered.to_csv('tweets_demojified1.tsv', sep='\t', index=False)

### Separating the demojified strings with spaces

# Defining a function to separate the demojified strings with spaces
def preprocess_line(input_line):
    # Add a space before the first delimiter '<em>', if it is not already preceded by one
    preprocessed_line = re.sub(r'(?<! )<em>', ' <em>', input_line)
    # Add a space after the first delimiter '<em>', if it is not already followed by one
    preprocessed_line = re.sub(r'<em>(?! )', '<em> ', preprocessed_line)
    return preprocessed_line

# Separating the demojified strings with spaces
df_tweets_filtered['Text'] = df_tweets_filtered['Text'].apply(preprocess_line)

#### Exporting the filtered data into a file for inspection

df_tweets_filtered.to_csv('tweets_demojified2.tsv', sep='\t', index=False)

### Formatting the demojified strings

# Defining a function to format the demojified string
def format_demojified_string(input_line):
    # Defining a function to format the demojified string using RegEx
    def process_demojified_string(s):
            # Lowercase the string
            s = s.lower()
            # Replace spaces and colons followed by a space with underscores
            s = re.sub(r'(: )| ', '_', s)
            # Add the appropriate prefixes and suffixes
            s = f'EMOJI{s}e'
            return s

    # Use RegEx to find and process each demojified string
    processed_line = re.sub(r'<em>(.*?)<em>', lambda match: process_demojified_string(match.group(1)), input_line)
    return processed_line

# Formatting the demojified strings
df_tweets_filtered['Text'] = df_tweets_filtered['Text'].apply(format_demojified_string)

### Replacing the `pipe` character by the `-` character in the `text` column

#Further on, a few columns of the dataframe are going to be exported into the file `tweets.txt` whose columns need to be delimited by the `pipe` character. Therefore, it is recommended that any occurrences of the `pipe` character in the `text` column are replaced by another character.

# Defining a function to replace the 'pipe' character by the '-' character
def replace_pipe_with_hyphen(input_string):
    modified_string = re.sub(r'\|', '-', input_string)
    return modified_string

# Replacing the 'pipe' character by the '-' character
df_tweets_filtered['Text'] = df_tweets_filtered['Text'].apply(replace_pipe_with_hyphen)

#### Exporting the filtered data into a file for inspection

df_tweets_filtered.to_csv('tweets_demojified3.tsv', sep='\t', index=False)

## Tokenising

#Please refer to [What is tokenization in NLP?](https://www.analyticsvidhya.com/blog/2020/05/what-is-tokenization-nlp/).

# Defining a function to tokenise a string
def tokenise_string(input_line):
    # Replace URLs with placeholders
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\b'
    placeholder = '<URL>'  # Choose a unique placeholder
    urls = re.findall(url_pattern, input_line)
    tokenised_line = re.sub(url_pattern, placeholder, input_line)  # Replace URLs with placeholders
    
    # Replace curly quotes with straight ones
    tokenised_line = tokenised_line.replace('“', '"').replace('”', '"').replace("‘", "'").replace("’", "'")
    # Separate common punctuation marks with spaces
    tokenised_line = re.sub(r'([.\!?,"\'/()])', r' \1 ', tokenised_line)
    # Add a space before '#'
    tokenised_line = re.sub(r'(?<!\s)#', r' #', tokenised_line)  # Add a space before '#' if it is not already preceded by one
    # Reduce extra spaces by a single space
    tokenised_line = re.sub(r'\s+', ' ', tokenised_line)
    
    # Replace the placeholders with the respective URLs
    for url in urls:
        tokenised_line = tokenised_line.replace(placeholder, url, 1)
    
    return tokenised_line

# Tokenising the strings
df_tweets_filtered['Text'] = df_tweets_filtered['Text'].apply(tokenise_string)

## Creating the files `file_index.txt` and `tweets.txt`

### Creating column `text_id`

df_tweets_filtered['text_id'] = 't' + df_tweets_filtered.index.astype(str).str.zfill(6)

### Creating column `conversation`

#The column `conversation` maps on the column `Title`.

df_tweets_filtered['conversation'] = 'v:' + df_tweets_filtered['Title']

#### Replacing space by the `_` character

#**Important**: Since the strings in the original columns contain spaces, Pandas creates `file_index.txt` with the columns enclosed with `"` - this caracter causes issues in `examples.sh` when it is executed. Therefore, spaces should be replaced by another character such as underscore.

# Defining a function to replace space by the '_' character
def replace_space_with_underscore(input_string):
    modified_string = re.sub(r' ', '_', input_string)
    return modified_string

# Replacing space by the '_' character
df_tweets_filtered['conversation'] = df_tweets_filtered['conversation'].apply(replace_space_with_underscore)

### Creating column `date`

#The column `date` maps on the column `Date`.

# Extract the date part (without time) into a new column 'date'
df_tweets_filtered['date'] = df_tweets_filtered['Date'].dt.date

# Add the prefix 'd:' to the 'date' values
df_tweets_filtered['date'] = 'd:' + df_tweets_filtered['date'].astype(str)

### Creating column `text_url`

#The column `text_url` maps on the column `Debate`.

df_tweets_filtered['text_url'] = 'url:' + df_tweets_filtered['Debate']

#### Replacing space by the `_` character

# Replacing space by the '_' character
df_tweets_filtered['text_url'] = df_tweets_filtered['text_url'].apply(replace_space_with_underscore)

### Creating column `user`

#The column `user` maps on the column `Speaker`.

df_tweets_filtered['user'] = 'u:' + df_tweets_filtered['Speaker']

#### Replacing space by the `_` character

# Replacing space by the '_' character
df_tweets_filtered['user'] = df_tweets_filtered['user'].apply(replace_space_with_underscore)

### Creating column `content`

#The column `content` maps on the column `Text`.

df_tweets_filtered['content'] = 'c:' + df_tweets_filtered['Text']

### Reordering the created columns

#Please refer to:
#- [Python - List Comprehension 1](https://www.w3schools.com/python/python_lists_comprehension.asp)
#- [Python - List Comprehension 2](https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/)

# Reorder the columns (we use list comprehension to create a list of all columns except 'text_id', 'variable', 'date' and 'text_url')
df_tweets_filtered = df_tweets_filtered[['text_id', 'conversation', 'date', 'text_url', 'user', 'content'] + [col for col in df_tweets_filtered.columns if col not in ['text_id', 'conversation', 'date', 'text_url', 'user', 'content']]]

df_tweets_filtered

### Creating the file `file_index.txt`

df_tweets_filtered[['text_id', 'conversation', 'date', 'text_url']].to_csv('file_index.txt', sep=' ', index=False, header=False, encoding='utf-8', lineterminator='\n')

### Creating the file `tweets.txt`

folder = 'tweets'
try:
    os.mkdir(folder)
    print(f'Folder {folder} created!')
except FileExistsError:
    print(f'Folder {folder} already exists')

#Note: The parameters `doublequote=False` and `escapechar=' '` are required to avoid that the column content is doublequoted with '"' in sentences that use characters that need to be escaped such as double quote '"' itself - this causes a malformed response from TreeTagger.

df_tweets_filtered[['text_id', 'conversation', 'date', 'user', 'content']].to_csv(f'{folder}/tweets.txt', sep='|', index=False, header=False, encoding='utf-8', lineterminator='\n', doublequote=False, escapechar=' ')
