#include <pybind11/pybind11.h>
#include "tracer_tool.h"

void init() {
  tracer_init();
}

void start() {
  tracer_start();
}

void stop() {
  tracer_stop();
}


PYBIND11_MODULE(pytracer, m) {
  m.doc() = "pytracer";

  init();
  m.def("init", &init);
  m.def("start", &start);
  m.def("stop", &stop);
}
