def dibujar_bidon(porcentaje, longitud_chorro):
    porcentaje = max(0, min(100, porcentaje))
    longitud_chorro = max(8, min(220, longitud_chorro))

    html = f"""
    <div style="display:flex; align-items:center; gap:0px; margin-top:10px;">

        <div style="
            width:220px;
            height:420px;
            border:5px solid #FFFFFF;
            border-radius:25px;
            position:relative;
            overflow:hidden;
            background:#E8F4FA;
        ">

            <div style="
                position:absolute;
                bottom:0;
                left:0;
                width:100%;
                height:{porcentaje}%;
                background:linear-gradient(180deg, #42A5F5, #1E88E5);
                transition:height 0.4s ease;
            "></div>

            <div style="
                position:absolute;
                right:-2px;
                bottom:55px;
                width:18px;
                height:18px;
                background:#111827;
                border-radius:50%;
                border:3px solid white;
                z-index:5;
            "></div>

            <div style="
                position:absolute;
                top:10px;
                left:15px;
                color:#0F172A;
                font-weight:bold;
                font-size:14px;
                z-index:6;
            ">
                {porcentaje:.1f}%
            </div>

        </div>

        <div style="
            width:{longitud_chorro}px;
            height:8px;
            background:#4FC3F7;
            border-radius:10px;
            margin-top:250px;
            transition:width 0.4s ease;
        "></div>

    </div>
    """

    return html
