// Data dummy untuk tanaman
const plants = [
    { name: "Padi", description: "Cocok untuk daerah beriklim tropis dengan curah hujan tinggi." },
    { name: "Jagung", description: "Dapat tumbuh di daerah panas dan dataran rendah." },
    { name: "Kopi", description: "Ideal di daerah pegunungan dengan suhu sejuk." },
    { name: "Cabe", description: "Membutuhkan tanah yang subur dengan sinar matahari penuh." },
    { name: "Kentang", description: "Baik di daerah pegunungan dengan tanah berpasir." }
];

// Fungsi untuk menampilkan daftar tanaman
function displayPlants(data) {
    const plantList = document.getElementById('plant-list');
    plantList.innerHTML = ''; // Hapus konten sebelumnya

    data.forEach(plant => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<span>${plant.name}:</span> ${plant.description}`;
        plantList.appendChild(listItem);
    });
}

// Fungsi untuk pencarian tanaman
function searchPlant() {
    const query = document.getElementById('search').value.toLowerCase();
    const filteredPlants = plants.filter(plant =>
        plant.name.toLowerCase().includes(query)
    );
    displayPlants(filteredPlants);
}

// Tampilkan semua tanaman saat halaman dimuat
window.onload = () => {
    displayPlants(plants);
};