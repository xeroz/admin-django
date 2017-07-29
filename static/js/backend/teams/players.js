$(document).ready(function () {
    var country = $('#country')
    var team_id = $('#team_id')
    var row = $('#row')
    var detail = $('#detail')
    var player_id = $('#player_id')
    var pace = $('#pace')
    var shooting = $('#shooting')
    var passing = $('#passing')
    var dribbling = $('#dribbling')
    var defending = $('#defending')
    var physical = $('#physical')

    var filterByCountry = function () {
        var data = {
            "country": $("#country option:selected").val(),
            "team_id": team_id.val(),
        };
        $.ajax({
            url: '/teams/get_players_by_country/',
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

    var getDetailPlayer = function() {
        var player_id = $(this).attr("id");
        var data = {
            "player_id": player_id,
        };

        $.ajax({
            url: '/teams/get_detail_player/',
            type: 'get',
            data: data,
        }).done(function (player) {
            // pace field
            var progress_pace = progress(player[0].fields.pace)
            pace.html('');
            pace.append(progress_pace);
            // shooting field
            var progress_shooting = progress(player[0].fields.shooting)
            shooting.html('');
            shooting.append(progress_shooting);
            // shooting field
            var progress_passing = progress(player[0].fields.passing)
            passing.html('');
            passing.append(progress_passing);
            // dribbling field
            var progress_dribbling = progress(player[0].fields.dribbling)
            dribbling.html('');
            dribbling.append(progress_dribbling);
            // defending field
            var progress_defending = progress(player[0].fields.defending)
            defending.html('');
            defending.append(progress_defending);
            // physical field
            var progress_physical = progress(player[0].fields.physical)
            physical.html('');
            physical.append(progress_physical);
            $('#myModal').modal('show');
        });

    }

    function progress(progress_field)
    {
        var array = '<div class="progress">'+
                    '<div role="progressbar" aria-valuenow="'+progress_field+'" aria-valuemin="0"'+
                    ' aria-valuemax="100" style="width: '+progress_field+'%" class="progress-bar progress-bar-info">'+
                    '</div>'+
                    '</div>';
        return array;
    }

    $(document).on('click', '.detail', getDetailPlayer);
    country.change(filterByCountry);
});