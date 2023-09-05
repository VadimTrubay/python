#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import datetime as DT

from flask import Flask, render_template_string
from common import get_crash_statistics_list_db


app = Flask(__name__)


@app.route('/')
def index():
    headers = ["Дата", "ДТП", "Погибли", "Погибло детей", "Ранены", "Ранено детей"]
    rows = get_crash_statistics_list_db()
    rows.reverse()

    data = []
    for date, dtp, died, children_died, wounded, wounded_children in rows:
        data.append({
            'date': date,
            'date_iso': DT.datetime.strptime(date, '%d.%m.%Y').date().isoformat(),
            'dtp': int(dtp),
            'died': int(died),
            'children_died': int(children_died),
            'wounded': int(wounded),
            'wounded_children': int(wounded_children),
        })

    return render_template_string("""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta content='text/html; charset=UTF-8' http-equiv='Content-Type'/>
    <title>{{ title }}</title>

    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='bootstrap-4.3.1/bootstrap.min.css') }}">

    <script src="{{ url_for('static', filename='js/jquery-3.1.1.min.js') }}"></script>
    <script src="{{ url_for('static', filename='bootstrap-4.3.1/bootstrap.min.js') }}"></script>
    <script src="{{ url_for('static', filename='chart_js_2.9.3/Chart.bundle.min.js') }}"></script>
    <style>
        .table-wrap {
            height: 90vh;
            overflow-y: auto;
        }
    </style>
</head>
<body>
<div class="container-fluid">
    <h2 class="text-center"><a href="https://гибдд.рф/">{{ title }}</a></h2>

    <div class="row">
        <div class="col-5 table-wrap">
            <table class="table table-hover">
                <thead class="thead-dark">
                    <tr>
                    {% for header in headers %}
                        <th>{{ header }}</th>
                    {% endfor %}
                    </tr>
                </thead>
                <tbody></tbody>
            </table>
        </div>
        <div class="col-7">
            <canvas id="lineChart"></canvas>
        </div>
    </div>
</div>
<script>
    let data = {{ data | safe }};

    $(document).ready(function() {
        let labels = [];
        let data_dtp = [];
        let data_died = [];
        let data_children_died = [];
        let data_wounded = [];
        let data_wounded_children = [];
    
        let table = $('table > tbody');
        
        for (let x of data) {
            let tr = $('<tr>')
                .append($(`<td>${x.date}</td>`))
                .append($(`<td>${x.dtp}</td>`))
                .append($(`<td>${x.died}</td>`))
                .append($(`<td>${x.children_died}</td>`))
                .append($(`<td>${x.wounded}</td>`))
                .append($(`<td>${x.wounded_children}</td>`))
            ;
            table.append(tr);
            
            labels.push(x.date_iso);
            data_dtp.push({
                x: x.date_iso,
                y: x.dtp,
            });
            data_died.push({
                x: x.date_iso,
                y: x.died,
            });
            data_children_died.push({
                x: x.date_iso,
                y: x.children_died,
            });
            data_wounded.push({
                x: x.date_iso,
                y: x.wounded,
            });
            data_wounded_children.push({
                x: x.date_iso,
                y: x.wounded_children,
            });
        }
    
        var ctx = document.getElementById("lineChart").getContext("2d");
        var lineChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'ДТП',
                        lineTension: 0,
                        borderColor: "red",
                        data: data_dtp,
                    },
                    {
                        label: 'Погибли',
                        lineTension: 0,
                        borderColor: "rgb(246, 139, 31)",
                        data: data_died,
                    },
                    {
                        label: 'Погибло детей',
                        lineTension: 0,
                        borderColor: "rgb(68, 44, 110)",
                        data: data_children_died,
                    },
                    {
                        label: 'Ранены',
                        lineTension: 0,
                        borderColor: "blue",
                        data: data_wounded,
                    },
                    {
                        label: 'Ранено детей',
                        lineTension: 0,
                        borderColor: "green",
                        data: data_wounded_children,
                    },
                ],
            },
            options: {
                scales: {
                    xAxes: [{
                        type: 'time',
                        time: {
                            unit: 'month',
                            tooltipFormat: 'DD/MM/YYYY',
                            displayFormats: {
                               day: 'DD/MM/YY'
                            }
                        },
                        distribution: 'linear'
                    }]
                }
            }
        });
    });
</script>
</body>
</html>
    """, title="АВАРИЙНОСТЬ НА ДОРОГАХ РОССИИ", headers=headers, data=data
)


if __name__ == "__main__":
    app.debug = True

    # Localhost
    app.run(port=10009)

    # # Public IP
    # app.run(host='0.0.0.0')
