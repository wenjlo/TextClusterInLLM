import plotly.express as px


def get_n_colors_from_plotly_scale(n, scale_name='Plotly'):
    """
    Returns n distinct colors from a specified Plotly qualitative color scale.
    Available scales in plotly.express.colors.qualitative:
    'Plotly', 'D3', 'G10', 'T10', 'Alphabet', 'Dark24', 'Light24',
    'Set1', 'Paired', 'Dark2', 'Accent', 'Vivid', 'Bold', 'Pastel'
    """
    # plotly.express.colors.qualitative has the color lists
    available_scales = {
        'Plotly': px.colors.qualitative.Plotly
    }

    if scale_name not in available_scales:
        raise ValueError(f"Invalid scale_name. Choose from: {list(available_scales.keys())}")
    colors_list = available_scales[scale_name]
    selected_colors = [colors_list[i % len(colors_list)] for i in range(n)]
    return selected_colors