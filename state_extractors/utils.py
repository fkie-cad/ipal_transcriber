from state_extractors.default import DefaultStateExtractor
from state_extractors.timeslice import TimeSliceStateExtractor

# Keep list up-to-date with all implemented state extractors!
all_state_extractors = [
    DefaultStateExtractor,
    TimeSliceStateExtractor,
]


def get_all_state_extractors():
    return {
        state_extractor._name: state_extractor
        for state_extractor in all_state_extractors
    }
