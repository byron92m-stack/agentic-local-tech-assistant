# Ejemplos de Uso del Agente Técnico Local

Este documento muestra ejemplos reales de interacción con el **Agente Conversacional Técnico Local**, incluyendo su flujo cognitivo interno:

```
Orchestrator → Validator → Respuesta final
```

Los ejemplos están diseñados para demostrar claridad técnica, razonamiento verificable y utilidad práctica.

---

## 1. Ejemplo: Explicar WSL2

### **Input del usuario**
> Explica cómo funciona WSL2 y en qué se diferencia de WSL1.

---

### **Salida del agente**

#### **Orchestrator**
- Explicar qué es WSL1.  
- Explicar qué es WSL2.  
- Comparar arquitectura: traducción de syscalls vs kernel real.  
- Comparar rendimiento, compatibilidad y uso de disco.  
- Dar una conclusión clara.

#### **Validator**
- Confirmar que la explicación no asume acceso a internet.  
- Verificar que la comparación sea técnica y precisa.  
- Asegurar claridad para un usuario técnico.

#### **Respuesta final**
WSL1 traduce llamadas del kernel Linux a llamadas de Windows, lo que lo hace rápido para operaciones simples pero limitado en compatibilidad.  
WSL2 ejecuta un kernel Linux real dentro de una VM ligera, ofreciendo compatibilidad completa, mejor rendimiento en Docker, mejor manejo de archivos y un entorno Linux auténtico.  
La principal diferencia es que WSL2 **no emula** Linux: lo ejecuta de forma nativa dentro de una micro‑VM.

---

## 2. Ejemplo: Diagnóstico técnico

### **Input del usuario**
> Mi WSL2 está lento al acceder a archivos en `/mnt/c`. ¿Qué puede ser?

---

### **Salida del agente**

#### **Orchestrator**
- Identificar causas comunes: latencia del filesystem, antivirus, I/O bridging.  
- Explicar por qué `/mnt/c` es lento.  
- Proponer mitigaciones.  

#### **Validator**
- Confirmar que las recomendaciones no impliquen acciones peligrosas.  
- Asegurar que las causas estén correctamente explicadas.

#### **Respuesta final**
El acceso a `/mnt/c` es lento porque WSL2 debe traducir operaciones NTFS ↔ Linux, lo que introduce latencia.  
Además, antivirus y herramientas de indexado pueden bloquear operaciones.  
La solución es trabajar dentro de `~/` siempre que sea posible, mover proyectos a Linux y evitar builds pesados en `/mnt/c`.

---

## 3. Ejemplo: Diseño de arquitectura

### **Input del usuario**
> Diseña una arquitectura mínima para un ETL que procese datos de Bitcoin y los cargue en ClickHouse.

---

### **Salida del agente**

#### **Orchestrator**
- Identificar componentes: ingestor, almacenamiento raw, transformaciones, carga.  
- Proponer formato: Parquet.  
- Proponer motor OLAP: ClickHouse.  
- Describir flujo.  

#### **Validator**
- Confirmar que el diseño sea reproducible y local.  
- Evitar dependencias externas.  
- Asegurar claridad en cada etapa.

#### **Respuesta final**
Una arquitectura mínima incluye:  
1. **Ingestor RPC** que consulta `bitcoind` y escribe snapshots en Parquet.  
2. **Almacén raw** particionado por rango de bloques.  
3. **Transformador** que normaliza y valida datos.  
4. **Cargador** que inserta en ClickHouse usando MergeTree.  
5. **Control de estado** en Postgres para manejar reorgs y checkpoints.  

Es modular, reproducible y funciona 100% en local.

---

## 4. Ejemplo: Auditoría de entorno

### **Input del usuario**
> ¿Cómo verifico si mi instalación de WSL2 está usando virtualización por hardware?

---

### **Salida del agente**

#### **Orchestrator**
- Explicar qué requiere WSL2.  
- Proponer comandos de verificación.  
- Explicar cómo interpretar resultados.  

#### **Validator**
- Confirmar que los comandos sean seguros.  
- Asegurar que no impliquen cambios en el sistema.

#### **Respuesta final**
Puedes verificarlo ejecutando en PowerShell:

```
systeminfo | find "Virtualization"
```

Si aparece “Virtualization Enabled In Firmware: Yes”, entonces WSL2 está usando virtualización por hardware.  
También puedes revisar:

```
wsl --status
```

para confirmar que el kernel y la plataforma están activos.

---

## 5. Ejemplo: Documentación técnica

### **Input del usuario**
> Explica la diferencia entre un Orchestrator y un Validator dentro del agente.

---

### **Salida del agente**

#### **Orchestrator**
- Definir ambos roles.  
- Explicar su interacción.  
- Dar un ejemplo práctico.

#### **Validator**
- Confirmar que la explicación sea clara y no redundante.  
- Asegurar que el ejemplo sea correcto.

#### **Respuesta final**
El **Orchestrator** propone un plan: pasos, estrategias y análisis.  
El **Validator** revisa ese plan, detecta riesgos, corrige inconsistencias y valida la respuesta final.  
Trabajan en secuencia para producir razonamiento claro y seguro.

---

Estos ejemplos muestran cómo razona el agente y cómo estructura sus respuestas.
