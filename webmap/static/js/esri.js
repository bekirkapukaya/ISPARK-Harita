require([
  'esri/config',
  'esri/Map',
  'esri/views/MapView',
  'esri/layers/GeoJSONLayer',
], function (esriConfig, Map, MapView, GeoJSONLayer) {
  esriConfig.apiKey =
    'AAPKf94de7daa0b74102b335646db409fe1eWPc-QIXS_ReACE9vzyHvvEO_ePxgewANyZ9yVKH40NMpFu6-1nv-ss3lXZrLvX-L';

  let url = "http://localhost:8000/getpoints"

  const geojsonLayer = new GeoJSONLayer({
    url: url,
    copyright: 'ISPARK',
  });

  const map = new Map({
    basemap: 'arcgis-topographic',
    layers:[geojsonLayer]
  });

  const view = new MapView({
    map: map,
    center: [28.977, 41.013],
    zoom: 13,
    container: 'viewDiv',
  });
});
