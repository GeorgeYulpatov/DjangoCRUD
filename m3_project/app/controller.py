from objectpack.observer import (
    ObservableController,
    Observer,
)

observer = Observer()
controller = ObservableController(
    url='actions',
    observer=observer,
)
