# 2024-MS-DS-11
import pandas as pd

data = pd.read_csv('LinkFire.csv')


#  1. Total pageview events and per day
def pageviews(data):
    pageview_events = data[data['event'] == 'pageview'].copy()  
    total_pageviews = pageview_events.shape[0]

    pageview_events['date'] = pd.to_datetime(pageview_events['date'])
    pageviews_per_day = pageview_events.groupby(by="date")["event"].count()
    return total_pageviews, pageviews_per_day


# 2. Total number of other recorded events
# 2. Total number of other recorded events
def analyze_events(data):
    event_name = set(data['event'].unique())
    event_name.remove("pageview")
    for event in event_name:
        total_events= data[data['event']== event].shape[0]
        print("total " , event ,"events is" , total_events, "\n")

        # Group by date
        event_perday = data[data['event']== event].groupby(by="date")["event"].count()

        print(event , "event per day:\n" , event_perday ,"\n")
    
# 3. Countries where the pageviews came from
def pageviews_by_country(data):
    pageview_events = data[data['event'] == 'pageview']
    pageviews_by_country = pageview_events.groupby('country').size().sort_values(ascending=False)
    
    return pageviews_by_country


# 4. Overall click rate (clicks/pageviews)
def calculate_click_rate(data):
    total_clicks = data[data['event'] == 'click'].shape[0]
    total_pageviews = data[data['event'] == 'pageview'].shape[0]
    click_rate = total_clicks / total_pageviews if total_pageviews > 0 else 0
    return click_rate

# 5. Clickrate distribution across different links
def clickrate_by_link(data):
    link_group = data.groupby('linkid').event.value_counts().unstack(fill_value=0)
    link_group['clickrate'] = link_group['click'] / link_group['pageview']
    return link_group[['click', 'pageview', 'clickrate']]

def main():
    # 1. Total pageviews and per day
    total_pageviews, pageviews_per_day = pageviews(data)
    print("Total pageviews", total_pageviews)
    print("Pageviews per day:")
    print(pageviews_per_day)


    # 2. Total number of other recorded events
    analyze_events(data)

    # 3. Countries where the pageviews originated
    pageviews_country = pageviews_by_country(data)
    print("\nPageviews by country:")
    print(pageviews_country)

    # 4. Overall click rate (clicks/pageviews)
    click_rate = calculate_click_rate(data)
    print("\nOverall click rate(clicks/pageviews)",click_rate)

    # 5. Clickrate distribution across different links
    clickrate_distribution = clickrate_by_link(data)
    print("\nClick rate distribution by link:")
    print(clickrate_distribution)

main()