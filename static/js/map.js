require([
  'esri/config',
  'esri/Map',
  'esri/views/MapView',
  'esri/layers/GeoJSONLayer',
  'esri/widgets/Legend',
  'esri/widgets/Expand',
  'esri/widgets/Home',
  'esri/widgets/LayerList',
  'esri/widgets/BasemapToggle',
  'esri/widgets/ScaleBar',
  'esri/widgets/Compass',
  'esri/PopupTemplate',
  'esri/popup/content/CustomContent',
], function (
  esriConfig,
  Map,
  MapView,
  GeoJSONLayer,
  Legend,
  Expand,
  Home,
  LayerList,
  BasemapToggle,
  ScaleBar,
  Compass,
  PopupTemplate,
  CustomContent
) {
  esriConfig.apiKey =
    'AAPKf94de7daa0b74102b335646db409fe1eWPc-QIXS_ReACE9vzyHvvEO_ePxgewANyZ9yVKH40NMpFu6-1nv-ss3lXZrLvX-L';

  let url = 'http://localhost:8000/map/getpoints';

  const clusterConfig = {
    type: 'cluster',
    clusterRadius: '100px',
    popupTemplate: {
      content: 'Bu nokta kümesi {cluster_count} tane durak içermektedir.',
      fieldInfos: [
        {
          fieldName: 'cluster_count',
          format: {
            places: 0,
            digitSeparator: true,
          },
        },
      ],
    },
    clusterMinSize: '24px',
    clusterMaxSize: '60px',
    labelingInfo: [
      {
        deconflictionStrategy: 'none',
        labelExpressionInfo: {
          expression: "Text($feature.cluster_count, '#,###')",
        },
        symbol: {
          type: 'text',
          color: '#004a5d',
          font: {
            weight: 'bold',
            family: 'Noto Sans',
            size: '12px',
          },
        },
        labelPlacement: 'center-center',
      },
    ],
  };

  const layer = new GeoJSONLayer({
    title: 'ISPARK Duraklar',
    url: url,
    copyright: 'İBB',
    featureReduction: clusterConfig,
    popupTemplate: {
      title: 'ISPARK Durak Bilgisi',
      content: [
        {
          type: 'text',
          text: '{parkName} durağı bilgisi',
        },
        {
          type: 'fields',
          fieldInfos: [
            {
              label: 'Park ID',
              fieldName: 'parkId',
            },
            {
              label: 'Park Adi',
              fieldName: 'parkName',
            },
            {
              label: 'Lokasyon ID',
              fieldName: 'locationId',
            },
            {
              label: 'Lokasyon Kodu',
              fieldName: 'locationCode',
            },
            {
              label: 'Lokasyon Adi',
              fieldName: 'locationName',
            },
            {
              label: 'Park Tipi ID',
              fieldName: 'parkTypeId',
            },
            {
              label: 'Park Tipi',
              fieldName: 'parkType',
            },
            {
              label: 'Park Kapasitesi',
              fieldName: 'parkCapacity',
            },
            {
              label: 'Calisma Saatleri',
              fieldName: 'workHours',
            },
            {
              label: 'Bolge ID',
              fieldName: 'regionId',
            },
            {
              label: 'Bolge',
              fieldName: 'region',
            },
            {
              label: 'Alt Bolge ID',
              fieldName: 'subRegionId',
            },
            {
              label: 'Alt Bolge',
              fieldName: 'subRegion',
            },
            {
              label: 'Ilce ID',
              fieldName: 'boroughld',
            },
            {
              label: 'Ilce',
              fieldName: 'borough',
            },
            {
              label: 'Adres',
              fieldName: 'address',
            },
            {
              label: 'Enlem',
              fieldName: 'lat',
            },
            {
              label: 'Boylam',
              fieldName: 'lon',
            },
            {
              label: 'Aylik Abonelik Ucreti',
              fieldName: 'monthlyPrice',
            },
            {
              label: 'Ucretsiz Parklanma Suresi (dakika)',
              fieldName: 'freeParkingTime',
            },
            {
              label: 'Tarifesi',
              fieldName: 'price',
            },
            {
              label: 'Park Et Devam Et Noktasi',
              fieldName: 'parkAndGoPoint',
            },
          ],
        },
        new CustomContent({
          outFields: ['*'],
          creator: function (event) {
            let parkId = event.graphic.attributes.parkId;
            let duzenleLink = document.createElement('a');
            let linkText = document.createTextNode('Düzenle');
            duzenleLink.appendChild(linkText);
            duzenleLink.className = 'btn btn-success';
            duzenleLink.style = 'width:100%';
            duzenleLink.title = 'Düzenle';
            duzenleLink.href = `http://localhost:8000/map/editlocation/${parkId}`;
            return duzenleLink;
          },
        }),
        new CustomContent({
          outFields: ['*'],
          creator: function (event) {
            let parkId = event.graphic.attributes.parkId;
            let silLink = document.createElement('a');
            let linkText = document.createTextNode('Sil');
            silLink.appendChild(linkText);
            silLink.className = 'btn btn-danger';
            silLink.style = 'width:100%';
            silLink.title = 'Sil';
            silLink.href = `http://localhost:8000/map/deletepoint/${parkId}`;
            return silLink;
          },
        }),
      ],
    },
    renderer: {
      type: 'simple',
      field: 'mag',
      symbol: {
        type: 'simple-marker',
        size: 4,
        color: '#69dcff',
        outline: {
          color: 'rgba(0, 139, 174, 0.5)',
          width: 5,
        },
      },
    },
  });

  const map = new Map({
    basemap: 'arcgis-navigation',
    layers: [layer],
  });

  const view = new MapView({
    map: map,
    center: [28.977, 41.013],
    zoom: 11,
    container: 'viewDiv',
  });

  view.ui.add(
    new Home({
      view: view,
    }),
    'top-left'
  );

  const layerList = new LayerList({
    view: view,
  });
  view.ui.add(layerList, {
    position: 'top-right',
  });

  const basemapToggle = new BasemapToggle({
    view: view,
    nextBasemap: 'streets-night-vector',
  });

  view.ui.add(basemapToggle, 'bottom-right');

  const scaleBar = new ScaleBar({
    view: view,
    unit:'dual'
  });
  view.ui.add(scaleBar, {
    position: 'bottom-left',
  });

  const legend = new Legend({
    view: view,
    container: 'legendDiv',
  });

  const compass = new Compass({
    view: view,
  });

  view.ui.add(compass, 'top-left');

  const infoDiv = document.getElementById('infoDiv');

  view.ui.add(
    new Expand({
      view: view,
      content: infoDiv,
      expandIconClass: 'esri-icon-layer-list',
      expanded: false,
    }),
    'top-left'
  );

  const toggleButton = document.getElementById('cluster');

  toggleButton.addEventListener('click', function () {
    let fr = layer.featureReduction;
    layer.featureReduction = fr && fr.type === 'cluster' ? null : clusterConfig;
    toggleButton.innerText =
      toggleButton.innerText === 'Kümelemeyi Aç'
        ? 'Kümelemeyi Kapat'
        : 'Kümelemeyi Aç';
  });
});
