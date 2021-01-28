<template>
<div class='row'>
    <div class='col-md-4'>
        <ul class="list-group">
            <li class="list-group-item" v-for="(site, index) in sites" :key="index">
                <router-link :to="`/graph/${site.name}`">{{site.name}}</router-link>
            </li>
        </ul>
    </div>
</div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            sites : [],
            errors : [],
        };
    },
    created() {
         axios.get('http://127.0.0.1:8000/api/sites/')
            .then( response => {
                this.sites = response.data;
                console.log(response.data);
            })
            .catch( e => {
                this.errors.push(e);
            });
    },

}
</script>