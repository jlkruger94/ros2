# kruger_guariste_pkg

## Autores

- José Luis Krüger
- Juan Manuel Guariste

Este paquete reproduce un rosbag descargado desde [https://catalog.ngc.nvidia.com/orgs/nvidia/teams/isaac/resources/r2bdataset2023/files] y lanza automáticamente RViz y RQT para visualizar su contenido. Nos interesó el dataset por su utilidad para visualizar sensores en un entorno real.

# Cmd de obtención del dataset:

```bash
curl -L 'https://api.ngc.nvidia.com/v2/resources/org/nvidia/team/isaac/r2bdataset2023/3/files?redirect=true&path=r2b_storage/r2b_storage_0.db3' -o 'r2b_storage/r2b_storage_0.db3'

curl -L 'https://api.ngc.nvidia.com/v2/resources/org/nvidia/team/isaac/r2bdataset2023/3/files?redirect=true&path=r2b_storage/metadata.yaml' -o 'r2b_storage/metadata.yaml'
```

## Uso

```bash
ros2 launch kruger_guariste_pkg rosbag_rviz_rqt.launch.py
```

