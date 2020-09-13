
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **religious events or traditions** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **religious events or traditions**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **religious events or traditions**?  For this category you might consider calendar events, demographic data about religion in the region and neighboring regions, participation in religious events, or how religious events relate to political events, social movements, or historical events.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[2]:

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib notebook')


# In[3]:

plt.style.use('seaborn-colorblind')
Snowfall = pd.read_csv('UNdata_Snowfall.csv')
Snowfall.head()


# In[ ]:

Temperature = pd.read_excel('Temp_1961_1990.xls')
Rainfall = pd.read_excel('Rain_1961_1990.xls')


# In[ ]:

Jan = Snowfall['Jan'].mean()
Feb = Snowfall['Feb'].mean()
Mar = Snowfall['Mar'].mean()
Apr = Snowfall['Apr'].mean()
May = Snowfall['May'].mean()
Jun = Snowfall['Jun'].mean()
Jul = Snowfall['Jul'].mean()
Aug = Snowfall['Aug'].mean()
Sep = Snowfall['Sep'].mean()
Oct = Snowfall['Oct'].mean()
Nov = Snowfall['Nov'].mean()
Dec = Snowfall['Dec'].mean()


# In[ ]:

Weather = pd.DataFrame({'Snowfall': [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]})


# In[ ]:

Monthly_Temp = Temperature.groupby(' Month').mean()['tas']
Jan = Monthly_Temp.iloc[0]
Feb = Monthly_Temp.iloc[1]
Mar = Monthly_Temp.iloc[2]
Apr = Monthly_Temp.iloc[3]
May = Monthly_Temp.iloc[4]
Jun = Monthly_Temp.iloc[5]
Jul = Monthly_Temp.iloc[6]
Aug = Monthly_Temp.iloc[7]
Sep = Monthly_Temp.iloc[8]
Oct = Monthly_Temp.iloc[9]
Nov = Monthly_Temp.iloc[10]
Dec = Monthly_Temp.iloc[11]


# In[ ]:

Weather['Temperature'] = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]


# In[ ]:

Monthly_Rain = Rainfall.groupby(' Month').mean()['pr']
Monthly_Rain.iloc[0]
Jan = Monthly_Rain.iloc[0]
Feb = Monthly_Rain.iloc[1]
Mar = Monthly_Rain.iloc[2]
Apr = Monthly_Rain.iloc[3]
May = Monthly_Rain.iloc[4]
Jun = Monthly_Rain.iloc[5]
Jul = Monthly_Rain.iloc[6]
Aug = Monthly_Rain.iloc[7]
Sep = Monthly_Rain.iloc[8]
Oct = Monthly_Rain.iloc[9]
Nov = Monthly_Rain.iloc[10]
Dec = Monthly_Rain.iloc[11]


# In[ ]:

Weather['Rainfall'] = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]


# In[ ]:

Weather['Snowfall'] = Weather['Snowfall']/1000
Weather.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


# In[ ]:

x = Weather.index.tolist()
y1 = Weather['Snowfall'].tolist()
y2 = Weather['Temperature'].tolist()
y3 = Weather['Rainfall'].tolist()

plt.plot(x, y1, '-s', label = "Snowfall (in 0.1*m)")
plt.plot(x, y2, '-*', label = "Temperature (in $\,^{\circ}\mathrm{C}$)")
plt.plot(x, y3, '-o', label = "Rainfall (in 0.1*cm)")

plt.title('Average Temperature, Snowfall and Rainfall in United States(1961-1990)')
 
plt.legend(frameon=False)
[plt.gca().spines[loc].set_visible(False) for loc in ['top', 'right']]

plt.show()

