<template>
  <div class="container">
    <h4>Données pour le site : {{this.site}}</h4>
      <b-form-row>
        <b-col md=4><b-form-select v-model="selected" :options="options" v-on:change="set_chartdata"/></b-col>
      </b-form-row>
      <b-form-row>
        <b-col md=4><b-form-datepicker placeholder="Selectionner une date de début" v-model="date_min" /></b-col>
        <b-col md=4><b-form-timepicker placeholder="Selectionner une heure de début" v-model="time_min" /></b-col>
      </b-form-row>
      <b-form-row>
        <b-col md=4><b-form-datepicker placeholder="Selectionner une date de fin" v-model="date_max" /></b-col>
        <b-col md=4><b-form-timepicker placeholder="Selectionner une heure de fin" v-model="time_max" /></b-col>
      </b-form-row>
      <b-form-row>
        <b-col md=2><b-button v-on:click="request_data">Afficher</b-button></b-col>
      </b-form-row>
    <div class='row'>
      <div class='col-md-12'>
        <div class="error-message" v-if="showError">
          {{ errorMessage }}
        </div>
        <line-chart v-if="loaded" :chart-data="chartdata"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import LineChart from './LineChart.js'

export default {
  name: 'LineGraphContainer',
  components: { LineChart },
  data(){ 
    return {
      selected: null,
      date_min: "",
      time_min: "",
      date_max: "",
      time_max: "",
      site: "",
      options : [
        { value: null, text : 'Selectionner un paramètre', disabled: true},
        { value: 'pression', text: 'Pression'},
        { value: 'temp', text: 'Température'},
        { value: 'humidity', text : "Pourcentage d'Humidité"},
        { value: 'wind', text: 'Vitesse du vent'},
      ],
      loaded: false,
      data: [],
      chartdata: null,
      showError: false,
      errorMessage: ''
    };
  },
  mounted () {
      this.site = this.$route.params.name;
      this.request_data();
  },

  methods: {
    request_data() {
      this.showError = false;
      if (!(this.valid_input(this.selected) && this.valid_input(this.date_min)
          && this.valid_input(this.date_max))){
            this.showError = true;
            this.errorMessage = "Il faut séléctionner un paramètre et une plage de dates"
            return;
      }
      this.loaded = false;
      axios.get(`http://127.0.0.1:8000/api/data/?date_min=${this.date_min}&time_min=${this.time_min}&date_max=${this.date_max}&time_max=${this.time_max}&site=${this.site}`)
      .then ( response => {
          if (response.data.length == 0) {
            this.showError = true;
            this.errorMessage = 'Erreur : Pas de données enregistrées pour ce site et sur cette plage de date';
          } else {
            this.loaded = true;
            this.data = response.data;
            this.set_chartdata(this.selected);
          }
      })
      .catch (e => {
        this.showError = true;
        this.errorMessage = e;
      });
    },
    
    set_chartdata(selected){
      if (this.loaded) {
        this.chartdata = {
          labels : this.data.map(elem => elem.date),
          datasets: [{
            label : selected,
            borderWidth: 1,
            pointBorderColor: "#3380ff",
            borderColor: "#83b2ff",
            backgroundColor: "transparent",
            data: this.select_param(selected, this.data)
           }]
        };
      }
      console.log()
    },    
    
    valid_input(input) {
      if (input === null || input === '' || input === 'undefined') {
        return false;
      } else {
        return true;
      }
    },
    
    select_param(selected, data) {
      if(!(this.valid_input(selected) && this.valid_input(this.date_min)
          && this.valid_input(this.date_max))) {
        return;
      }
      switch(selected) {
        case 'temp':
          return data.map(elem => elem.temp);
        case 'pression':
          return data.map(elem => elem.pression);
        case 'humidity':
          return data.map(elem => elem.humidity);
        case 'wind':
          return data.map(elem => elem.wind);
      }
      return;
    }
  }
}
</script>
