<template>
  <div>
    <h3 class="mb-4 text-gray-700 font-medium text-3xl">SLO Configuration</h3>
    <SLOForm :data="sloData" @saved="saveConfig()" @reset="resetConfig()">
      <template v-slot:header>
        <div class="mb-2 m-2 text-right font-bold text-indigo-600">
          {{ sloData._relpath }}
        </div>
      </template>
      <template v-slot:buttons>
        <button
          @click="this.testConfig()"
          class="bg-indigo-500 hover:bg-indigo-800 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transform hover:scale-110 motion-reduce:transform-none"
        >
          Test
        </button>
      </template>

      <!-- Footer -->
      <template v-slot:footer>
        <div class="text-green-500" v-if="formSavedOnDisk">All changes saved to disk.</div>
        <div class="text-red-600" v-else-if="!formSavedSuccess">
          {{ formSavedError }}
        </div>
        <div class="text-orange-600" v-else>There are some unsaved changes.</div>

          <div class="text-green-500" v-if="configTestedSuccess">
            {{ configTestSuccessMessage }}
            <!-- {{ configTestData }} -->
          </div>
          <div class="text-red-600" v-else>
            {{ configTestErrorMessage }}
          </div>
      </template>
    </SLOForm>

    <!-- Git diff -->
    <div v-if="sloGitDiff != ''">
      <h4 class="text-gray-700 text-3xl font-medium">Git diff</h4>
      <div class="mt-5 p-5 bg-white shadow-md rounded">
        <div v-for="line in sloGitDiff.split('<br>')" :key="line">
          <div v-if="line.startsWith('-')" class="bg-red-300" v-html="line"></div>
          <div
            v-else-if="line.startsWith('+')"
            class="bg-green-200"
            v-html="line"
          ></div>
          <div v-else v-html="line"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import SLOCard from "../components/SLOCard.vue";
import SLOForm from "../components/SLOForm.vue";

export default defineComponent({
  data() {
    return {
      name: this.$route.params.name,
      firstPageLoad: true,
      saved: true,
      formSavedSuccess: true,
      formSavedOnDisk: true,
      formSavedError: "",
      sloData: {},
      sloGitDiff: "",
      configTestedSuccess: true,
      configTestErrorMessage: "",
      configTestSuccessMessage: "",
      configTestData: {}
    };
  },
  mounted() {
    this.firstPageLoad = true;
    this.fetchSloData();
    this.fetchGitDiff();
  },
  watch: {
    sloData: {
      handler(val) {
        this.formSavedError = "";
        if (!this.firstPageLoad) {
          this.formSavedOnDisk = false;
        }
        this.firstPageLoad = false;
      },
      deep: true,
    },
  },
  methods: {
    snakeToCamel(str) {
      return str.replace(/([-_][a-z])/g, (group) =>
        group.toUpperCase().replace("-", "").replace("_", "")
      );
    },
    async saveConfig() {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.sloData),
      };
      fetch(`/api/slo/${this.name}`, requestOptions)
        .then((res) => res.json())
        .then((resJson) => {
          this.configTested = false;
          this.configTestErrorMessage = "";
          if (resJson.success) {
            this.formSavedOnDisk = true;
            this.formSavedSuccess = true;
            // this.sloData = resJson.data;
            this.fetchGitDiff();
          } else {
            this.formSavedOnDisk = false;
            this.formSavedSuccess = false;
            this.formSavedError = resJson.errorMessage;
          }
        });
    },
    async testConfig(){
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.sloData),
      };
      this.saveConfig();
      this.configTestSuccessMessage = "Testing in progress ..."
      fetch(`/api/slo/${this.name}/test`, requestOptions)
        .then((res) => res.json())
        .then((resJson) => {
          console.log(resJson);
          if (resJson.success){
            this.configTestedSuccess = true;
            this.configTestSuccessMessage = "Config tested succesfully !"
            this.configTestData = resJson.data;
          } else {
            this.configTestedSuccess = false;
            this.configTestErrorMessage = resJson.errorMessage;
          }
        });
    },
    async fetchSloData() {
      fetch(`/api/slo/${this.name}`)
        .then((res) => res.json())
        .then((resJson) => {
          this.sloData = resJson;
        });
    },
    async fetchGitDiff() {
      fetch(`/api/slo/${this.name}/diff`)
        .then((res) => res.json())
        .then((resJson) => {
          this.sloGitDiff = resJson.diff.replace(new RegExp("\n", "g"), "<br>");
        });
    },
  },
  components: {
    SLOCard,
    SLOForm,
  },
});
</script>
