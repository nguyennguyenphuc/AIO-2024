def min_max_scaling(data1, data2, data3):
    """Normalize data using Min-Max scaling."""
    max_data = [max(data1), max(data2), max(data3)]
    min_data = [min(data1), min(data2), min(data3)]
    scaled_data1 = [(x - min_data[0]) / (max_data[0] - min_data[0]) for x in data1]
    scaled_data2 = [(x - min_data[1]) / (max_data[1] - min_data[1]) for x in data2]
    scaled_data3 = [(x - min_data[2]) / (max_data[2] - min_data[2]) for x in data3]
    return (scaled_data1, scaled_data2, scaled_data3), (*max_data, *min_data)
