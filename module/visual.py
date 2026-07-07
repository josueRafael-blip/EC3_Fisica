def dibujar_bidon(porcentaje, longitud_chorro):

    agua = f"""
    <div style="
        position:absolute;
        bottom:0;
        width:100%;
        height:{porcentaje}%;
        background:#2196F3;
        transition:1s;
    "></div>
    """

    html = f"""

    <div style="display:flex;align-items:center;">

        <div style="
            width:220px;
            height:420px;
            border:5px solid white;
            border-radius:20px;
            position:relative;
            overflow:hidden;
            background:#ececec;
        ">

            {agua}

        </div>

        <div style="
            width:{longitud_chorro}px;
            height:8px;
            background:#4FC3F7;
            margin-left:5px;
            border-radius:10px;
        ">

        </div>

    </div>

    """

    return html
