$(document).ready(function () {
    var country = $('#country')
    var team_id = $('#team_id')
    var row = $('#row')

    var filterByCountry = function () {

        var data = {
            "country": $("#country option:selected").val(),
            "team_id": team_id.val(),
        };
        $.ajax({
            url: 'http://127.0.0.1:8000/teams/get_players_by_country/',
            type: 'get',
            data: data,
        }).done(function (players) {
            row.html('');
            $.each(players, function (i) {
                row.append(
                    '<div class="col-md-4">' +
                    '<div class="panel widget">' +
                    '<div class="row row-table row-flush">' +
                    '<div class="col-xs-5">' +
                    '<picture class="lateral-picture">' +
                    '<img src="/media/' + players[i].fields.image + '" alt="">' +
                    '</picture>' +
                    '</div>' +
                    '<div class="col-xs-7 align-middle p-lg">' +
                    '<div class="pull-right"><a href="#" >' +
                    '<span class="label label-primary pull-right">' +
                    '<h4>' + players[i].fields.number + '</h4>' +
                    '</span></a>' +
                    '</div>' +
                    '<p>' +
                    '<h3>' + players[i].fields.name + ' ' + players[i].fields.lastname + '</h3>' +
                    '<strong>' + players[i].fields.position + '</strong>' +
                    '<p>' + players[i].fields.country + '</p>' +
                    '</p>' +
                    '</div>' +
                    '</div>' +
                    '</div>' +
                    '</div>'
                );
            });
        });
    }

    country.change(filterByCountry);
});