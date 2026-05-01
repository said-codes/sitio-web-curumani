<template>
  <section id="directorio" class="py-20 bg-surface-container-low px-8">
    <div class="max-w-7xl mx-auto">
      <div class="text-center mb-16">
        <h2 class="font-h1 text-h1 text-primary">Comercio del Barrio</h2>
        <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mx-auto mt-4">Descubre los mejores productos y servicios locales en nuestro mapa interactivo.</p>
      </div>
      
      <div class="bg-white rounded-2xl overflow-hidden shadow-lg h-[600px] flex flex-col md:flex-row relative">
        <!-- Sidebar List -->
        <div class="w-full md:w-1/3 h-64 md:h-full bg-surface-container-lowest border-r border-slate-200 overflow-y-auto p-4 flex flex-col gap-4 relative z-10 shadow-md">
          <div v-if="loading" class="flex justify-center p-8">
            <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
          </div>
          
          <div v-for="negocio in negocios" :key="negocio.id" 
               class="p-4 border border-slate-100 rounded-xl hover:bg-slate-50 cursor-pointer transition-colors shadow-sm"
               @click="centerMap(negocio)">
            <span class="inline-block px-2 py-1 bg-secondary text-white text-[10px] font-bold rounded-full mb-2 uppercase">{{ negocio.categoria }}</span>
            <h4 class="text-primary font-bold">{{ negocio.nombre }}</h4>
            <p class="text-sm text-slate-500 mt-1 flex items-center gap-1">
              <span class="material-symbols-outlined text-[14px]">location_on</span> {{ negocio.direccion }}
            </p>
            <p class="text-sm text-slate-500 flex items-center gap-1 mt-1">
              <span class="material-symbols-outlined text-[14px]">phone</span> {{ negocio.telefono }}
            </p>
          </div>
        </div>
        
        <!-- Map Container -->
        <div class="w-full md:w-2/3 h-full z-0 relative">
          <div id="business-map" class="w-full h-full"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// We will inject Leaflet dynamically to avoid SSR/bundler issues in standard setups, 
// but since we have it via npm, we can import it.
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

const negocios = ref([])
const loading = ref(true)
let map = null
let markers = []

const initMap = () => {
  map = L.map('business-map').setView([9.2025, -73.5550], 15)
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
  }).addTo(map)
}

const addMarkers = () => {
  // Clear old markers
  markers.forEach(m => map.removeLayer(m))
  markers = []

  const customIcon = L.divIcon({
    className: 'custom-div-icon',
    html: `<div style="background-color: #005A8D; width: 24px; height: 24px; border-radius: 50%; border: 3px solid #F4B533; box-shadow: 0 2px 5px rgba(0,0,0,0.3);"></div>`,
    iconSize: [24, 24],
    iconAnchor: [12, 12]
  })

  negocios.value.forEach(negocio => {
    const marker = L.marker([negocio.lat, negocio.lng], { icon: customIcon }).addTo(map)
    const popupContent = `
      <div class="p-2">
        <strong class="text-[#005A8D] text-lg block mb-1">${negocio.nombre}</strong>
        <p class="text-xs text-slate-600 mb-1">${negocio.direccion}</p>
        <p class="text-xs text-slate-600">${negocio.horario}</p>
      </div>
    `
    marker.bindPopup(popupContent)
    markers.push(marker)
  })
}

const centerMap = (negocio) => {
  if (map) {
    map.flyTo([negocio.lat, negocio.lng], 18, {
      duration: 1.5
    })
  }
}

onMounted(async () => {
  initMap()
  
  try {
    // Configura aquí la URL de tu backend en producción
    const baseUrl = 'http://127.0.0.1:8000'
    const response = await axios.get(`${baseUrl}/api/negocios/`)
    negocios.value = response.data
    addMarkers()
  } catch (error) {
    console.error('Error loading businesses:', error)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
/* Fix Leaflet z-index issues with Tailwind */
#business-map {
  z-index: 1;
}
</style>
