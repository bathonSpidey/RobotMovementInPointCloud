## A class for all filters that we might need
import pyrealsense2 as rs
class Processor:
    def get_decimation_filter(granularity = 1):
        decimation_filter = rs.decimation_filter()
        decimation_filter.set_option(rs.option.filter_magnitude, granularity)
        return decimation_filter