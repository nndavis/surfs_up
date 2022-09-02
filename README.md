# surfs_up
 SQLite SQLalchemy

## Overview of the analysis
This project is intended to provide temperature trends in hawaii for the months of June and December. This info is wanted so a shop owner can determine if the surf and ice cream shop business is sustainable year-round. Meaning, if the weather stays warm enough year round then these will be viable businesses. 
## Results
I was able to pull temperature data from a provided sqlite file that was made into a database. With this I used jupyter notebook to import the data and then filtered my data. Once the data was filtered I was then able to create dataframes using pandas. For those dataframes I created a column for date and a column for temp. After that I used df.describe() to print out a summary of statistics. 
- June
  - Minimum Temp: 64*F
  - Maximum Temp: 85*F
  - Mean Temp: 74.94*F
- December
  - Minimum Temp: 56*F
  - Maximum Temp: 83*F
  - Mean Temp: 71.04*F

Looking at some key temperature points, I would say the most important one to look at is the mean temperature. This shows the average temperature for the month, and the data shows that there is only a ~4* difference from June and December. Both of which are in the 70s, which is prime ice cream eating weather. As for the minimum temps, the difference here is greater as December bottoms at 56* while June bottoms at 64*. 56* is far too cold for ice cream and surfing, but 64* is feasible. The two share the smallest difference within maximum temperatures with it only being 2*. June peaks at 85* while December peaks at 83*. This is minimal, and both are great temperatures for surfing and ice cream.

## Summary
From what we know so far, it seems like both months are great for surf and icecream shops. Both have average temperatures in the 70s, and decent peak temperatures. Looking a bit deeper though, we can look into the %25 STD. This means only 25% of the data is below said temperature. Decembers 25% STD is 69*F. Meaning that 25% of the month is below 69*F. So if 70*F and higher is the days for best business, then a quarter of December will not be viable for business. To compare Junes 25% STD, we are looking at 73*F. 73* is a decent temperature to be at, and with 25% being below that there shouldn't be too much of a worry. Although, 64*F is quite low for June. I ran a count query for temperatures below 68* in the month of June. There are only 17 days that are below 68*. So 64* is quite the outlier for June, so it shouldn't be anything to worry about. Overall, Hawaii is a viable state to run a surf shop and ice cream shop year round.


