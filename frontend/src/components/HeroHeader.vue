<template>
  <div>
    <!-- TopNavBar -->
    <nav class="sticky top-0 w-full z-[100] bg-white/95 backdrop-blur-md border-b border-slate-100 shadow-sm">
      <div class="flex justify-between items-center h-20 px-4 md:px-8 max-w-7xl mx-auto">
        <div class="flex items-center gap-4">
          <span class="text-lg md:text-xl font-black text-[#005A8D] truncate max-w-[200px] md:max-w-none">Curumaní Cesar - Barrio El Paraíso</span>
        </div>
        
        <!-- Mobile Menu Button -->
        <button @click="isMobileMenuOpen = !isMobileMenuOpen" class="lg:hidden text-[#005A8D] p-2 focus:outline-none">
          <span class="material-symbols-outlined text-3xl">{{ isMobileMenuOpen ? 'close' : 'menu' }}</span>
        </button>

        <!-- Desktop Navigation -->
        <div class="hidden lg:flex items-center gap-8">
          <a class="font-['Public_Sans'] text-sm font-bold tracking-wide text-[#005A8D] border-b-2 border-[#005A8D] pb-1" href="#">Inicio</a>
          <a class="font-['Public_Sans'] text-sm font-medium tracking-wide text-slate-600 hover:text-[#005A8D] transition-all cursor-pointer" href="#noticias">Noticias</a>
          <a class="font-['Public_Sans'] text-sm font-medium tracking-wide text-slate-600 hover:text-[#005A8D] transition-all cursor-pointer" href="#conocer-curumani">Curumaní</a>
          <a class="font-['Public_Sans'] text-sm font-medium tracking-wide text-slate-600 hover:text-[#005A8D] transition-all cursor-pointer" href="#directorio">Directorio</a>
          <a class="font-['Public_Sans'] text-sm font-medium tracking-wide text-slate-600 hover:text-[#005A8D] transition-all cursor-pointer" href="#calendario">Calendario</a>
          <a class="font-['Public_Sans'] text-sm font-medium tracking-wide text-slate-600 hover:text-[#005A8D] transition-all cursor-pointer" href="#servicios">Servicios</a>
        </div>
        
        <div class="hidden lg:flex items-center gap-4">
          <div class="flex items-center gap-2 px-4 py-2 bg-[#005A8D]/10 border border-[#005A8D] rounded-full">
            <span class="material-symbols-outlined text-[#005A8D] text-sm">handshake</span>
            <span class="text-xs font-bold text-[#005A8D] tracking-tight">Comunidad UNAD</span>
          </div>
        </div>
      </div>

      <!-- Mobile Navigation Menu -->
      <div v-show="isMobileMenuOpen" class="lg:hidden absolute top-20 left-0 w-full bg-white border-b border-slate-100 shadow-lg py-4 px-4 flex flex-col gap-4">
        <a @click="isMobileMenuOpen = false" class="font-['Public_Sans'] text-base font-bold text-[#005A8D] block py-2" href="#">Inicio</a>
        <a @click="isMobileMenuOpen = false" class="font-['Public_Sans'] text-base font-medium text-slate-600 block py-2" href="#noticias">Noticias</a>
        <a @click="isMobileMenuOpen = false" class="font-['Public_Sans'] text-base font-medium text-slate-600 block py-2" href="#conocer-curumani">Sobre Curumaní</a>
        <a @click="isMobileMenuOpen = false" class="font-['Public_Sans'] text-base font-medium text-slate-600 block py-2" href="#directorio">Directorio Local</a>
        <a @click="isMobileMenuOpen = false" class="font-['Public_Sans'] text-base font-medium text-slate-600 block py-2" href="#calendario">Calendario</a>
        <a @click="isMobileMenuOpen = false" class="font-['Public_Sans'] text-base font-medium text-slate-600 block py-2" href="#servicios">Gestión Ciudadana</a>
        
        <div class="mt-4 pt-4 border-t border-slate-100 flex justify-center">
          <div class="flex items-center gap-2 px-4 py-2 bg-[#005A8D]/10 border border-[#005A8D] rounded-full inline-flex">
            <span class="material-symbols-outlined text-[#005A8D] text-sm">handshake</span>
            <span class="text-xs font-bold text-[#005A8D] tracking-tight">Comunidad UNAD</span>
          </div>
        </div>
      </div>
    </nav>
    
    <!-- Hero Section -->
    <header class="relative h-[500px] md:h-[600px] flex items-center overflow-hidden">
      <div class="absolute inset-0 z-0">
        <img class="w-full h-full object-cover" data-alt="A wide panoramic view of a vibrant Colombian neighborhood community center at dusk. The warm golden hour sunlight bathes the modern brick buildings and lush green parks in a soft glow. Diverse groups of people are interacting harmoniously in a clean, professional urban setting. The overall mood is hopeful, communal, and progressive, featuring a palette of deep blues and sunset oranges." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBhbAn_TXU50m2QUs--S_0XwxDFhsxnlj7rQzSkpfaRk2DuxZOFEOfvpnwfAn_lRSudKXg0R0FNUUmRKS5J8LhQO7X0DlksGty7iP1RgdgvIivP7qk3U9uKNfhkjIZRh4rIhhrDzfvfcCU5iraqI_QDxqc77j-fuNHYP_Z-sIhb-2Flbgwcz2jdeurP0XE3SLi_enizBsGJ97rhZ2XCC82h_M12npc7eA1ttYpdyWdUoLrYXk03IgJdW17U2Pvpvb3q0Uoc2jvsq0SP"/>
        <div class="absolute inset-0 bg-gradient-to-r from-primary/80 to-transparent"></div>
        
        <!-- ThreeJS Canvas will go here eventually -->
        <div id="three-canvas-container" class="absolute inset-0 z-0 opacity-50 mix-blend-screen pointer-events-none"></div>
      </div>
      <div class="relative z-10 max-w-7xl mx-auto px-8 w-full">
        <div class="max-w-2xl">
          <h1 class="font-h1 text-h1 text-white mb-6">Bienvenidos al Barrio El Paraíso: Unidos por el Progreso</h1>
          <p class="font-body-lg text-body-lg text-white/90 mb-10">Construyendo una comunidad más fuerte, segura y conectada a través del Servicio Social UNAD.</p>
          <a href="#conocer-curumani" class="inline-flex bg-gradient-to-br from-[#005A8D] to-[#F39200] text-white font-semibold py-4 px-10 rounded-lg shadow-lg hover:scale-105 transition-transform items-center gap-3">
            Conocer Más <span class="material-symbols-outlined">arrow_forward</span>
          </a>
        </div>
      </div>
    </header>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import * as THREE from 'three'

const isMobileMenuOpen = ref(false)

onMounted(() => {
  // Simple ThreeJS implementation for MVP
  const container = document.getElementById('three-canvas-container');
  if (!container) return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, window.innerWidth / 600, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
  
  renderer.setSize(window.innerWidth, 600);
  container.appendChild(renderer.domElement);

  // Particles
  const particlesGeometry = new THREE.BufferGeometry();
  const particlesCount = 300;
  
  const posArray = new Float32Array(particlesCount * 3);
  for(let i = 0; i < particlesCount * 3; i++) {
      posArray[i] = (Math.random() - 0.5) * 10;
  }
  
  particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
  
  const material = new THREE.PointsMaterial({
      size: 0.05,
      color: 0xF4B533,
      transparent: true,
      opacity: 0.8
  });
  
  const particlesMesh = new THREE.Points(particlesGeometry, material);
  scene.add(particlesMesh);
  
  camera.position.z = 3;

  function animate() {
      requestAnimationFrame(animate);
      particlesMesh.rotation.y += 0.001;
      particlesMesh.rotation.x += 0.0005;
      renderer.render(scene, camera);
  }
  
  animate();

  window.addEventListener('resize', () => {
      camera.aspect = window.innerWidth / 600;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, 600);
  });
})
</script>
