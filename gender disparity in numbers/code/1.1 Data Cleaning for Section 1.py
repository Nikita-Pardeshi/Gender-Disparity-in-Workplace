# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:53:19 2022

@author: 14255
"""

import pandas as pd
import numpy as np
import os
import pycountry as pc

Country = [
    ('United States'),
    ('Afghanistan'),
    ('Albania'),
    ('Algeria'),
    ('American Samoa'),
    ('Andorra'),
    ('Angola'),
    ('Anguilla'),
    ('Antarctica'),
    ('Antigua And Barbuda'),
    ('Argentina'),
    ('Armenia'),
    ('Aruba'),
    ('Australia'),
    ('Austria'),
    ('Azerbaijan'),
    ('Bahamas'),
    ('Bahrain'),
    ('Bangladesh'),
    ('Barbados'),
    ('Belarus'),
    ('Belgium'),
    ('Belize'),
    ('Benin'),
    ('Bermuda'),
    ('Bhutan'),
    ('Bolivia'),
    ('Bosnia And Herzegowina'),
    ('Botswana'),
    ('Bouvet Island'),
    ('Brazil'),
    ('Brunei Darussalam'),
    ('Bulgaria'),
    ('Burkina Faso'),
    ('Burundi'),
    ('Cambodia'),
    ('Cameroon'),
    ('Canada'),
    ('Cape Verde'),
    ('Cayman Islands'),
    ('Central African Rep'),
    ('Chad'),
    ('Chile'),
    ('China'),
    ('Christmas Island'),
    ('Cocos Islands'),
    ('Colombia'),
    ('Comoros'),
    ('Congo'),
    ('Cook Islands'),
    ('Costa Rica'),
    ('Cote D`ivoire'),
    ('Croatia'),
    ('Cuba'),
    ('Cyprus'),
    ('Czech Republic'),
    ('Denmark'),
    ('Djibouti'),
    ('Dominica'),
    ('Dominican Republic'),
    ('East Timor'),
    ('Ecuador'),
    ('Egypt'),
    ('El Salvador'),
    ('Equatorial Guinea'),
    ('Eritrea'),
    ('Estonia'),
    ('Ethiopia'),
    ('Falkland Islands (Malvinas)'),
    ('Faroe Islands'),
    ('Fiji'),
    ('Finland'),
    ('France'),
    ('French Guiana'),
    ('French Polynesia'),
    ('French S. Territories'),
    ('Gabon'),
    ('Gambia'),
    ('Georgia'),
    ('Germany'),
    ('Ghana'),
    ('Gibraltar'),
    ('Greece'),
    ('Greenland'),
    ('Grenada'),
    ('Guadeloupe'),
    ('Guam'),
    ('Guatemala'),
    ('Guinea'),
    ('Guinea-bissau'),
    ('Guyana'),
    ('Haiti'),
    ('Honduras'),
    ('Hong Kong'),
    ('Hungary'),
    ('Iceland'),
    ('India'),
    ('Indonesia'),
    ('Iran'),
    ('Iraq'),
    ('Ireland'),
    ('Israel'),
    ('Italy'),
    ('Jamaica'),
    ('Japan'),
    ('Jordan'),
    ('Kazakhstan'),
    ('Kenya'),
    ('Kiribati'),
    ('Korea (North)'),
    ('Korea (South)'),
    ('Kuwait'),
    ('Kyrgyzstan'),
    ('Laos'),
    ('Latvia'),
    ('Lebanon'),
    ('Lesotho'),
    ('Liberia'),
    ('Libya'),
    ('Liechtenstein'),
    ('Lithuania'),
    ('Luxembourg'),
    ('Macau'),
    ('Macedonia'),
    ('Madagascar'),
    ('Malawi'),
    ('Malaysia'),
    ('Maldives'),
    ('Mali'),
    ('Malta'),
    ('Marshall Islands'),
    ('Martinique'),
    ('Mauritania'),
    ('Mauritius'),
    ('Mayotte'),
    ('Mexico'),
    ('Micronesia'),
    ('Moldova'),
    ('Monaco'),
    ('Mongolia'),
    ('Montserrat'),
    ('Morocco'),
    ('Mozambique'),
    ('Myanmar'),
    ('Namibia'),
    ('Nauru'),
    ('Nepal'),
    ('Netherlands'),
    ('Netherlands Antilles'),
    ('New Caledonia'),
    ('New Zealand'),
    ('Nicaragua'),
    ('Niger'),
    ('Nigeria'),
    ('Niue'),
    ('Norfolk Island'),
    ('Northern Mariana Islands'),
    ('Norway'),
    ('Oman'),
    ('Pakistan'),
    ('Palau'),
    ('Panama'),
    ('Papua New Guinea'),
    ('Paraguay'),
    ('Peru'),
    ('Philippines'),
    ('Pitcairn'),
    ('Poland'),
    ('Portugal'),
    ('Puerto Rico'),
    ('Qatar'),
    ('Reunion'),
    ('Romania'),
    ('Russian Federation'),
    ('Rwanda'),
    ('Saint Kitts And Nevis'),
    ('Saint Lucia'),
    ('St Vincent/Grenadines'),
    ('Samoa'),
    ('San Marino'),
    ('Sao Tome'),
    ('Saudi Arabia'),
    ('Senegal'),
    ('Seychelles'),
    ('Sierra Leone'),
    ('Singapore'),
    ('Slovakia'),
    ('Slovenia'),
    ('Solomon Islands'),
    ('Somalia'),
    ('South Africa'),
    ('Spain'),
    ('Sri Lanka'),
    ('St. Helena'),
    ('St.Pierre'),
    ('Sudan'),
    ('Suriname'),
    ('Swaziland'),
    ('Sweden'),
    ('Switzerland'),
    ('Syrian Arab Republic'),
    ('Taiwan'),
    ('Tajikistan'),
    ('Tanzania'),
    ('Thailand'),
    ('Togo'),
    ('Tokelau'),
    ('Tonga'),
    ('Trinidad And Tobago'),
    ('Tunisia'),
    ('Turkey'),
    ('Turkmenistan'),
    ('Tuvalu'),
    ('Uganda'),
    ('Ukraine'),
    ('United Arab Emirates'),
    ('United Kingdom'),
    ('Uruguay'),
    ('Uzbekistan'),
    ('Vanuatu'),
    ('Vatican City State'),
    ('Venezuela'),
    ('Viet Nam'),
    ('Virgin Islands (British)'),
    ('Virgin Islands (U.S.)'),
    ('EH', 'Western Sahara'),
    ('Yemen'),
    ('Yugoslavia'),
    ('Zaire'),
    ('Zambia'),
    ('Zimbabwe'),
    ('Bahamas, The'),
    ('Antigua and Barbuda'),
    ('Bosnia and Herzegovina'),
    ('Cabo Verde'),
    ('Congo, Dem. Rep.'),
    ('Congo, Rep.'),
    ("Cote d'Ivoire"),
    ('Curacao'),
    ('Egypt, Arab Rep.'),
    ('Eswatini'),
    ('Gambia, The'),
    ('Guinea-Bissau'),
    ('Hong Kong SAR, China'),
    ('Iran, Islamic Rep.'),
    ('Isle of Man'),
    ("Korea, Dem. People's Rep."),
    ('Korea, Rep.'),
    ('Lao PDR'),
    ('Late-demographic dividend'),
    ('Macao SAR, China'),
    ('Micronesia, Fed. Sts.'),
    ('Montenegro'),
    ('North Macedonia'),
    ('Sao Tome and Principe'),
    ('Serbia'),
    ('Slovak Republic'),
    ('South Sudan'),
    ('St. Kitts and Nevis'),
    ('St. Lucia'),
    ('St. Vincent and the Grenadines'),
    ('Timor-Leste'),
    ('Trinidad and Tobago'),
    ('Venezuela, RB'),
    ('Vietnam'),
    ('Yemen, Rep.')
]


df = pd.read_csv(
    "../../datasets/Gender stat multiple years and series.csv")
print(df.head())

# delete columns with no value
#df = df.drop([col for col in df.columns if df[col].eq('..').all()], axis=1)
# df = df.replace({'..': np.nan})
# df = df.dropna(how='any')

colheaders = df.columns[4:].str[:4]
df.columns = ['Series Name', 'Series Code', 'Country Name', 'Country Code', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
              '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
              '2014', '2015', '2016', '2017', '2018', '2019', '2020']

df.drop(df.loc[df['1996'] == '..'].index, inplace=True)
df = df.replace({'..': ''})

# delete series code and country name
df = df.drop(['Series Code'], axis=1)


# reading second csv
df2 = pd.read_csv(
    "../../datasets/gender-inequality-index-from-the-human-development-report.csv")


# pivot wider
df2_wide = df2.pivot_table(index=["Entity", "Code"],
                           columns='Year',
                           values='Gender Inequality Index (Human Development Report (2015))').reset_index()


df2_wide["Series Name"] = 'Gender Inequality Index (Human Development Report (2015))'


# rename column headers to match with the first dataframe
df2_wide = df2_wide.rename(columns={
    "Entity": "Country Name",
    "Code": "Country Code"
})


# changing dtype of columns to ensure that concant happens without creating new columns if already present
df[['1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',       '2017', '2018', '2019', '2020']] = df[['1996', '1997', '1998',
                                                                                                                                                                                                                         '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
                                                                                                                                                                                                                         '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
                                                                                                                                                                                                                         '2017', '2018', '2019', '2020']].apply(pd.to_numeric)

# change column header to a string
df2_wide.columns = df2_wide.columns.astype(str)

df2_wide[['1995', '2000', '2005', '2010', '2011', '2012', '2013', '2014', '2015']] = df2_wide[[
    '1995', '2000', '2005', '2010', '2011', '2012', '2013', '2014', '2015']].apply(pd.to_numeric)

df3 = pd.concat([df, df2_wide], ignore_index=True)


# reading second csv
df4 = pd.read_csv(
    "../../datasets/Violence against women.csv")

# deleting columns not required
df4 = df4.drop(['Region', 'REGION', 'INC', 'VAR',
               'Flag Codes', 'Flags', 'TIME', 'Year'], axis=1)

# Combine Income and Var column
df4["Series Name"] = df4["Income"] + df4["Variable"]

# deleting income and variable column
df4 = df4.drop(['Income', 'Variable'], axis=1)

# rename year column to 2019
df4 = df4.rename(columns={
    "Value": "2019",
    "Country": "Country Name",
    "LOCATION": "Country Code"
})

# delete duplicate rows
# df4.drop_duplicates(keep=False,inplace=True)

df5 = df4.drop_duplicates(keep='first')

df6 = pd.concat([df3, df5], ignore_index=True)

df6.to_csv("abc6.csv")

# 3
df_gdp_gini = df6.loc[df6["Series Name"].isin(
    ["GDP growth (annual %)", "Gini index (World Bank estimate)", "Population, female (% of total)"])]
df_gdp_gini.head()

df_gdp_gini = df6


# displaying gdp and gini as columns
df_gdp_gini_long = pd.melt(df_gdp_gini, id_vars=['Country Name', 'Country Code', 'Series Name'], value_vars=['1996', '1997', '1998',
                                                                                                             '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
                                                                                                             '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
                                                                                                             '2017', '2018', '2019', '2020', '1995', ])

# rename column headers
df_gdp_gini_long = df_gdp_gini_long.rename(columns={
    "value": "value",
    "variable": "year",
    "Series Name": "series"
})


# making it wide
df_gdp_gini_wide = df_gdp_gini_long.pivot_table(
    index=['Country Name', 'Country Code', 'year'],
    columns='series',
    values='value').reset_index()


wb_grouping = df_gdp_gini_wide[df_gdp_gini_wide['Country Name'].isin(Country)]

# adding gdp
df7 = pd.read_csv(
    "../../datasets/gdp-per-capita-worldbank.csv")

# rename column headers
df7 = df7.rename(columns={
    "Entity": "Country Name",
    "Code": "Country Code",
    "Year": "year"
})


df7["year"] = df7["year"].astype(str)

new_df = pd.merge(wb_grouping, df7,  how='left', on=[
                  'Country Name', 'Country Code', 'year', ])
