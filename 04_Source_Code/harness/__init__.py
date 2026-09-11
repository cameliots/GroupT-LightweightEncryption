"""Experimental framework for the comparative evaluation.

Each module here corresponds to one component of the architecture in Figure 3.1
(see ``03_Architecture_and_Flowchart/Experimental_Architecture.md``):

===========================  ==========================================
Figure 3.1 component         Module
===========================  ==========================================
Experimental Control Module  ``control_module``
Performance Monitoring Unit  ``monitor``
Data Logger                  ``data_logger``
Analysis & Comparison        ``analysis``
Environment record           ``environment``
===========================  ==========================================
"""

from .control_module import RunConfig, run_experiment
from .data_logger import DataLogger
from .monitor import measure

__all__ = ["RunConfig", "run_experiment", "DataLogger", "measure"]
