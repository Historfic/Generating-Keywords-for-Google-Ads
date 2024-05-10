## 1. The brief
# List of words to pair with products

words = ['buy', 'price', 'discount', 'promo', 'shop', 'promos', 'pricing',
         'low price', 'purchase']

#print list of words
print(words)

## 2. Combine the words with the product names

products = ['sofas', 'convertible sofas',
            'love seats', 'recliners', 'sofa beds']

#Create an empty list
keywords_list = []

#Loop through products
for product in products:
    #Loop through words
    for word in words:
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])

from pprint import pprint
pprint(keywords_list)



## 3. Convert the list of lists into a DataFrame

import pandas as pd

keywords_df = pd.DataFrame.from_records(keywords_list)

print(keywords_df)

## 4. Rename the columns of the DataFrame

keywords_df = keywords_df.rename(columns={0: 'Ad Group', 1: 'Keyword'})


## 5. Add a campaign column
keywords_df['Campaign'] = 'SEM_Sofas'

## 6. Create the match type column

keywords_df['Criterion Type' ] = 'Exact'

## 7. Duplicate all the keywords into 'phrase' match

keywords_phrase = keywords_df.copy()

keywords_phrase['Criterion Type'] = 'Phrase'

keywords_df_final = keywords_df.append(keywords_phrase)

## 8. Save and summarize!

#Save
keywords_df_final.to_csv('Keywords.csv', index=0)

summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)