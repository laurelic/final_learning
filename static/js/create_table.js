var table = new Tabulator("#inpatient-table", {
    pagination: "local",
    paginationSize: 50,
    layout: "fitColumns",
    columns:[
        {title: "DRG Name", field: "drg_definition"},
        {title: "Prodiver ID", field: "provider_id"},
        {title: "Provider Name", field: "provider_name"},
        {title: "Provider Address", field: "provider_street_address"},
        {title: "Provider City", field: "provider_city"},
        {title: "Provider State", field: "provider_state"},
        {title: "Provider Zip", field: "provider_zip_code"},
        {title: "HRR Description", field: "hrr_description"},
        {title: "Total Discharges", field: "total_disch"},
        {title: "Avg Covered Charges", field: "average_covered_charges"}
    ],
});

d3.json("/inpatient_data", function(data) {
    console.log(data)
    table.setData(data);
});