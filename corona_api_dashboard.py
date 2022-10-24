from corona_api import get_current_corona_data
from corona_data_mapping import map_corona_data
from file_helper import save_data_to_file


data = get_current_corona_data()
current_corona_data = map_corona_data(data)

save_data_to_file(current_corona_data)
