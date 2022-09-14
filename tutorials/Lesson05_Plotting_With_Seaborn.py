

#####################################################################################################################
###################################  Pokemon Excercise ############################################################
##################################################################################################################

pokemon_input_file='/home/pliu/data_set/python_data_set/pandas_data_visu/Pokemon.csv'
pokemon=pd.read_csv(pokemon_input_file,index_col=0)

#print(pokemon.shape)
#print(pokemon.dtypes)

# Q1. count plot on pokemon num count group by generation
#sns.countplot(pokemon['Generation'],ax=ax)
#plt.show()

# Q2. kde plot on pokemon num group by HP
# a dist plot includes the kde (why)
# sns.distplot(pokemon['HP'])
# plt.show()

# Q3. jointplot on defence and attack
#
# sns.jointplot(x='Attack', y='Defense', data=pokemon)
# plt.show()

# Q4. hexplot on defence and attack
#sns.jointplot(x='Attack', y='Defense', data=pokemon, kind='hex',gridsize=20)
#plt.show()

# Q5. kde plot on HP and attack
#sns.kdeplot(pokemon.loc[:,['HP','Attack']])
#plt.show()

# Q6. box plot on attack group by legendary
# sns.boxplot(x='Legendary',y='Attack',data=pokemon,ax=ax)
# plt.show()

# Q7. violinplot on attack group by legendary
sns.violinplot(x='Legendary',y='Attack',data=pokemon,ax=ax)
plt.show()

"""
Conclusion

seaborn is one of the most important, if not the most important, data visualization tool in the Python data 
viz ecosystem. In this notebook we looked at what features and capacities seaborn brings to the table. 
There's plenty more that you can do with the library that we won't cover here or elsewhere in the tutorial; 
I highly recommend browsing the terrific seaborn Gallery page (https://seaborn.pydata.org/examples/index.html) 
to see more beautiful examples of the library in action.
"""