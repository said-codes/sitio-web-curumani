<template>
  <section id="calendario" class="py-20 bg-slate-50 px-8">
    <div class="max-w-7xl mx-auto">
      <div class="text-center mb-16">
        <span class="text-secondary font-label-md text-label-md uppercase tracking-widest">Eventos</span>
        <h2 class="font-h1 text-h1 text-primary mt-2">Agenda Comunitaria</h2>
        <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mx-auto mt-4">Mantente al tanto de todas las actividades, asambleas y jornadas de integración de nuestro municipio.</p>
      </div>

      <div class="bg-white rounded-3xl shadow-[0_8px_30px_rgb(0,0,0,0.04)] p-8 max-w-5xl mx-auto border border-slate-100">
        <div v-if="loading" class="flex justify-center p-12">
          <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
        </div>
        <!-- FullCalendar Container -->
        <div id="calendar" class="min-h-[500px]" :class="{ 'hidden': loading }"></div>
      </div>
    </div>

    <!-- Event Modal -->
    <div v-if="selectedEvent" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm p-4" @click.self="closeModal">
      <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full overflow-hidden transform transition-all">
        <div class="bg-primary p-6 text-white relative">
          <button @click="closeModal" class="absolute top-4 right-4 text-white/80 hover:text-white transition-colors">
            <span class="material-symbols-outlined">close</span>
          </button>
          <h3 class="text-2xl font-bold mb-2">{{ selectedEvent.title }}</h3>
          <div class="flex items-center gap-2 text-white/90 text-sm">
            <span class="material-symbols-outlined text-[18px]">calendar_today</span>
            {{ formatDate(selectedEvent.start) }}
          </div>
        </div>
        <div class="p-6">
          <p class="text-slate-600 mb-6">Detalles del evento comunitario. Te esperamos para seguir construyendo nuestro municipio.</p>
          <button @click="closeModal" class="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold py-3 px-6 rounded-xl transition-colors">
            Cerrar
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { Calendar } from '@fullcalendar/core'
import dayGridPlugin from '@fullcalendar/daygrid'
import listPlugin from '@fullcalendar/list'

const loading = ref(true)
const selectedEvent = ref(null)

const closeModal = () => {
  selectedEvent.value = null
}

const formatDate = (date) => {
  if (!date) return ''
  return new Date(date).toLocaleDateString('es-CO', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(async () => {
  try {
    // Configura aquí la URL de tu backend en producción
    // const baseUrl = import.meta.env.PROD ? 'https://curumani-backend.onrender.com' : 'http://127.0.0.1:8000'
    const baseUrl = 'https://sitio-web-curumani.onrender.com'
    const response = await axios.get(`${baseUrl}/api/eventos/`)
    const eventos = response.data

    const calendarEl = document.getElementById('calendar')
    if (calendarEl) {
      const calendar = new Calendar(calendarEl, {
        plugins: [dayGridPlugin, listPlugin],
        initialView: 'dayGridMonth',
        locale: 'es',
        headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,listWeek'
        },
        buttonText: {
          today: 'Hoy',
          month: 'Mes',
          list: 'Lista'
        },
        events: eventos,
        eventClick: function(info) {
          info.jsEvent.preventDefault();
          selectedEvent.value = {
            title: info.event.title,
            start: info.event.start
          }
        },
        height: 'auto',
        contentHeight: 600,
        dayMaxEvents: true,
        eventTimeFormat: {
          hour: '2-digit',
          minute: '2-digit',
          meridiem: 'short'
        }
      })
      calendar.render()
    }
  } catch (error) {
    console.error('Error loading events:', error)
  } finally {
    loading.value = false
  }
})
</script>

<style>
/* Custom FullCalendar Tailwind Overrides */
.fc {
  font-family: 'Public Sans', sans-serif;
  max-width: 100%;
}
.fc-view-harness {
  overflow-x: auto;
}
.fc-theme-standard th {
  padding: 16px 0;
  background-color: #f8fafc;
  color: #005A8D;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.875rem;
  letter-spacing: 0.05em;
  border-color: #e2e8f0;
}
.fc-theme-standard td {
  border-color: #e2e8f0;
}
.fc-event {
  cursor: pointer;
  border-radius: 6px;
  padding: 4px 8px;
  font-size: 0.75rem;
  border: none;
  box-shadow: 0 1px 2px rgba(0,0,0,0.1);
  transition: transform 0.2s;
  white-space: normal !important;
  word-wrap: break-word;
  line-height: 1.2;
}
.fc-event-main {
  white-space: normal !important;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
.fc-event:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  z-index: 5;
}
.fc-toolbar {
  flex-wrap: wrap;
  gap: 1rem;
}
.fc-toolbar-title {
  color: #005A8D;
  font-weight: 800 !important;
  font-size: 1.25rem !important;
}
@media (min-width: 768px) {
  .fc-toolbar-title {
    font-size: 1.5rem !important;
  }
  .fc-event {
    font-size: 0.85rem;
  }
}
.fc-button-primary {
  background-color: #005A8D !important;
  border-color: #005A8D !important;
  text-transform: capitalize;
  font-weight: 600 !important;
  padding: 6px 12px !important;
  border-radius: 8px !important;
  transition: all 0.2s !important;
  font-size: 0.875rem !important;
}
@media (min-width: 768px) {
  .fc-button-primary {
    padding: 8px 16px !important;
    font-size: 1rem !important;
  }
}
.fc-button-primary:hover {
  background-color: #004a75 !important;
  border-color: #004a75 !important;
  transform: translateY(-1px);
}
.fc-button-primary:not(:disabled).fc-button-active {
  background-color: #F39200 !important;
  border-color: #F39200 !important;
}
.fc-day-today {
  background-color: #f0f7ff !important;
}
.fc-daygrid-day-number {
  padding: 8px !important;
  font-weight: 500;
  color: #475569;
}
</style>
