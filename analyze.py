import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

training_set = pd.read_csv('optdigits.tra', header=None)
display(training_set.head())

testing_set = pd.read_csv('optdigits.tes', header=None)
display(testing_set.head())

pd.DataFrame(training_set.describe()[64])
pd.DataFrame(testing_set.describe()[64])

sns.distplot(training_set[64], kde = True, color ='red', bins = 30)
plt.show()
sns.distplot(testing_set[64], kde = True, color ='red', bins = 30)
plt.show()

display(pd.DataFrame(training_set.isnull().sum()))
display(pd.DataFrame(testing_set.isnull().sum()))