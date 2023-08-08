from m3_ext.context_processors import DesktopProcessor


def desktop(request):
  return DesktopProcessor.process(request)