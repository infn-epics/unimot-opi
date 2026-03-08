from org.csstudio.display.builder.runtime.script import PVUtil
from org.csstudio.display.builder.runtime.script import ScriptUtil

logger = ScriptUtil.getLogger()
pv = PVUtil.getString(pvs[0])
logger.info("MOTOR SELECTION:" + pv)

# pv is in the form "PREFIX:DEVICENAME" — split to get P and M
# Motor_Main.bob expects macros: P (prefix) and M (:devicename)
if pv:
    parts = pv.rsplit(":", 1)
    if len(parts) == 2:
        p_val = parts[0]
        m_val = ":" + parts[1]
        r_val = parts[1]
    else:
        p_val = pv
        m_val = ""
        r_val = ""

    widget.setPropertyValue("file", "")
    widget.getPropertyValue("macros").add("P", p_val)
    widget.getPropertyValue("macros").add("M", m_val)
    widget.getPropertyValue("macros").add("R", r_val)
    widget.getPropertyValue("macros").add("DEVICE", pv)
    widget.setPropertyValue("file", "Motor_Main.bob")
    logger.info("Motor device set: P=" + p_val + " M=" + m_val)
