import plotly.graph_objects as go


def say_do_to_html(
        grid_say_do:
        dict, cap_say_do:
        dict, all_say_do: dict
) -> str:
    fig = go.Figure(
        data=[
            go.Line(
                x=list(all_say_do.keys()),
                y=list(all_say_do.values()),
                name="All",
                line=dict(
                    color="seagreen",
                    width=6
                )
            ),
            go.Line(
                x=list(grid_say_do.keys()),
                y=list(grid_say_do.values()),
                name="Grid",
                visible='legendonly',
                line=dict(
                    color="cornflowerblue",
                    width=6
                )
            ),
            go.Line(
                x=list(cap_say_do.keys()),
                y=list(cap_say_do.values()),
                name="Cap",
                visible='legendonly',
                line=dict(
                    color="#F4D7C3",
                    width=6
                )
            )
        ],
        layout=go.Layout(
            title=go.layout.Title(text="Say Do")
        )
    )
    fig.update_xaxes(
        type='category',
        title_text='Sprints'
    )
    fig.update_yaxes(
        title_text='%'
    )
    fig.update_xaxes()
    return fig.to_html(include_plotlyjs='cdn', include_mathjax='cdn', full_html=False)


def velocity_to_html(
        grid_velocity: dict,
        cap_velocity: dict,
        all_velocity: dict
) -> str:
    fig = go.Figure(
        data=[
            go.Line(
                x=list(all_velocity.keys()),
                y=list(all_velocity.values()),
                name="All",
                line=dict(
                    color="seagreen",
                    width=6
                )
            ),
            go.Line(
                x=list(grid_velocity.keys()),
                y=list(grid_velocity.values()),
                name="Grid",
                visible='legendonly',
                line=dict(
                    color="cornflowerblue",
                    width=6
                )
            ),
            go.Line(
                x=list(cap_velocity.keys()),
                y=list(cap_velocity.values()),
                name="Cap",
                visible='legendonly',
                line=dict(
                    color="#F4D7C3",
                    width=6
                )
            )
        ],
        layout=go.Layout(
            title=go.layout.Title(text="Velocity")
        )
    )
    fig.update_xaxes(
        type='category',
        title_text='Sprints'
    )
    fig.update_yaxes(
        title_text='Resolved Issues'
    )
    fig.update_xaxes()
    return fig.to_html(include_plotlyjs='cdn', include_mathjax='cdn', full_html=False)


def accumulated_backlog_to_html(grid_do_acc, grid_say_acc, cap_do_acc, cap_say_acc, all_do_acc, all_say_acc) -> str:
    fig = go.Figure(
        data=[
            go.Line(
                x=list(all_do_acc.keys()),
                y=list(all_do_acc.values()),
                name="All Resolved",
                line=dict(
                    color="seagreen",
                    width=6
                )
            ),
            go.Line(
                x=list(all_say_acc.keys()),
                y=list(all_say_acc.values()),
                name="All Opened",
                line=dict(
                    color="MediumTurquoise",
                    width=6
                )
            ),
            go.Line(
                x=list(grid_do_acc.keys()),
                y=list(grid_do_acc.values()),
                name="Grid Resolved",
                visible='legendonly',
                line=dict(
                    color="cornflowerblue",
                    width=6
                )
            ),
            go.Line(
                x=list(grid_say_acc.keys()),
                y=list(grid_say_acc.values()),
                name="Grid Opened",
                visible='legendonly',
                line=dict(
                    color="MediumSlateBlue",
                    width=6
                )
            ),
            go.Line(
                x=list(cap_do_acc.keys()),
                y=list(cap_do_acc.values()),
                name="Cap Resolved",
                visible='legendonly',
                line=dict(
                    color="#F4D7C3",
                    width=6
                )
            ),
            go.Line(
                x=list(cap_say_acc.keys()),
                y=list(cap_say_acc.values()),
                name="Cap Opened",
                visible='legendonly',
                line=dict(
                    color="#EF9D5C",
                    width=6
                )
            )
        ],
        layout=go.Layout(
            title=go.layout.Title(text="Accumulated Backlog Created vs Resolved")
        )
    )
    fig.update_xaxes(
        type='category',
        title_text='Sprints'
    )
    fig.update_yaxes(
        title_text='Issues'
    )
    fig.update_xaxes()
    return fig.to_html(include_plotlyjs='cdn', include_mathjax='cdn', full_html=False)


def opened_bugs_to_html(
        grid_bugs: dict,
        cap_bugs: dict,
        all_bugs: dict
) -> str:
    fig = go.Figure(
        data=[
            go.Line(
                x=list(all_bugs.keys()),
                y=list(all_bugs.values()),
                name="All",
                line=dict(
                    color="seagreen",
                    width=6
                )
            ),
            go.Line(
                x=list(grid_bugs.keys()),
                y=list(grid_bugs.values()),
                name="Grid",
                visible='legendonly',
                line=dict(
                    color="cornflowerblue",
                    width=6
                )
            ),
            go.Line(
                x=list(cap_bugs.keys()),
                y=list(cap_bugs.values()),
                name="Cap",
                visible='legendonly',
                line=dict(
                    color="#F4D7C3",
                    width=6
                )
            )
        ],
        layout=go.Layout(
            title=go.layout.Title(text="Opened Defects")
        )
    )
    fig.update_xaxes(
        type='category',
        title_text='Sprints'
    )
    fig.update_yaxes(
        title_text='Issues'
    )
    fig.update_xaxes()
    return fig.to_html(include_plotlyjs='cdn', include_mathjax='cdn', full_html=False)


def bugs_by_adi_to_html(
        grid_bugs_by_adi: dict,
        cap_bugs_by_adi: dict,
        all_bugs_by_adi: dict
) -> str:
    fig = go.Figure(
        data=[
            go.Line(
                x=list(all_bugs_by_adi.keys()),
                y=list(all_bugs_by_adi.values()),
                name="All",
                line=dict(
                    color="seagreen",
                    width=6
                )
            ),
            go.Line(
                x=list(grid_bugs_by_adi.keys()),
                y=list(grid_bugs_by_adi.values()),
                name="Grid",
                visible='legendonly',
                line=dict(
                    color="cornflowerblue",
                    width=6
                )
            ),
            go.Line(
                x=list(cap_bugs_by_adi.keys()),
                y=list(cap_bugs_by_adi.values()),
                name="Cap",
                visible='legendonly',
                line=dict(
                    color="#F4D7C3",
                    width=6
                )
            )
        ],
        layout=go.Layout(
            title=go.layout.Title(text="Defects Opened by ADI")
        )
    )
    fig.update_xaxes(
        type='category',
        title_text='Sprints'
    )
    fig.update_yaxes(
        title_text='Issues'
    )
    fig.update_xaxes()
    return fig.to_html(include_plotlyjs='cdn', include_mathjax='cdn', full_html=False)


def counter_parts_to_html(grid_on_cap_acc: dict, cap_on_grid_acc: dict) -> str:
    fig = go.Figure(
        data=[
            go.Line(
                x=list(grid_on_cap_acc.keys()),
                y=list(grid_on_cap_acc.values()),
                name="Grid on Cap",
                visible='legendonly',
                line=dict(
                    color="cornflowerblue",
                    width=6
                )
            ),
            go.Line(
                x=list(cap_on_grid_acc.keys()),
                y=list(cap_on_grid_acc.values()),
                name="Cap on Grid",
                visible='legendonly',
                line=dict(
                    color="#F4D7C3",
                    width=6
                )
            )
        ],
        layout=go.Layout(
            title=go.layout.Title(text="Accumulated Defects Raised by counter parts")
        )
    )
    fig.update_xaxes(
        type='category',
        title_text='Sprints'
    )
    fig.update_yaxes(
        title_text='Bugs'
    )
    fig.update_xaxes()
    return fig.to_html(include_plotlyjs='cdn', include_mathjax='cdn', full_html=False)


def bugs_ratio_to_html(grid_ratio: dict, cap_ratio: dict, all_ratio: dict) -> str:
    fig = go.Figure(
        data=[
            go.Line(
                x=list(all_ratio.keys()),
                y=list(all_ratio.values()),
                name="All",
                line=dict(
                    color="seagreen",
                    width=6
                )
            ),
            go.Line(
                x=list(grid_ratio.keys()),
                y=list(grid_ratio.values()),
                name="Grid",
                visible='legendonly',
                line=dict(
                    color="cornflowerblue",
                    width=6
                )
            ),
            go.Line(
                x=list(cap_ratio.keys()),
                y=list(cap_ratio.values()),
                name="Cap",
                visible='legendonly',
                line=dict(
                    color="#F4D7C3",
                    width=6
                )
            )
        ],
        layout=go.Layout(
            title=go.layout.Title(text="Defects Ratio")
        )
    )
    fig.update_xaxes(
        type='category',
        title_text='Sprints'
    )
    fig.update_yaxes(
        title_text='Issues'
    )
    fig.update_xaxes()
    return fig.to_html(include_plotlyjs='cdn', include_mathjax='cdn', full_html=False)
