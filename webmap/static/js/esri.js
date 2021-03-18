require(['esri/config', 'esri/Map', 'esri/views/MapView'], function (
  esriConfig,
  Map,
  MapView
) {
  esriConfig.apiKey =
    'AAPKf94de7daa0b74102b335646db409fe1eWPc-QIXS_ReACE9vzyHvvEO_ePxgewANyZ9yVKH40NMpFu6-1nv-ss3lXZrLvX-L';

  const map = new Map({
    basemap: 'arcgis-topographic',
  });

  const view = new MapView({
    map: map,
    center: [-118.805, 34.027],
    zoom: 13,
    container: 'viewDiv',
  });
});
