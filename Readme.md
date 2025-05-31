# kruger_guariste_pkg

## Autores

- José Luis Krüger
- Juan Manuel Guariste

Este paquete reproduce un rosbag descargado desde [https://catalog.ngc.nvidia.com/orgs/nvidia/teams/isaac/resources/r2bdataset2023/files] y lanza automáticamente RViz y RQT para visualizar su contenido. Nos interesó el dataset por su utilidad para visualizar sensores en un entorno real.

## Uso

```bash
ros2 launch kruger_guariste_pkg rosbag_rviz_rqt.launch.py

