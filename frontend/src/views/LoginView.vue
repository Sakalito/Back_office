<template>
  <div class="login">
    <div class="login_content">
      <h2 class="login_title">Connexion</h2>
      <TextField
        :onChange="setUsername"
        hint="Nom d'utilisateur"
        :required="true"
        :validator="validateUsername"
      />
      <TextField
        :onChange="setPassword"
        hint="Mot de passe"
        type="password"
        :required="true"
        :validator="validatePassword"
      />
      <FlatButton text="Se connecter" :onTap="onLogin"></FlatButton>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapActions } from "vuex";
import TextField from "@/components/TextField.vue";
import FlatButton from "@/components/FlatButton.vue";

export default defineComponent({
  components: {
    TextField,
    FlatButton,
  },
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    ...mapActions(["login"]),
    setUsername(username: string) {
      this.username = username;
    },
    setPassword(password: string) {
      this.password = password;
    },
    validateUsername(username: string): string | null {
      if (username.length < 3) {
        return "Doit faire au moins 3 caractères";
      }
      return null;
    },
    validatePassword(password: string): string | null {
      if (password.length < 6) {
        return "Doit faire au moins 6 caractères";
      }
      return null;
    },
    async onLogin() {
      if (
        this.validateUsername(this.username) ||
        this.validatePassword(this.password)
      ) {
        console.log("Invalid login");
        return;
      }
      console.log("Logging in");
      this.login({ username: this.username, password: this.password }).then(
        (result) => {
          if (result.state) {
            this.$router.push({ name: "dashboard" });
          }
          /* this.$toasted.show(result.message, {
            position: "bottom-center",
            duration: 5000,
            theme: "bubble",
            type: result.state ? "success" : "error",
          }); */
        }
      );
    },
  },
});
</script>

<style>
body {
  background-color: #f5f5fa;
  display: block;
  align-items: center;
  height: 100%;
}

.login_title {
  margin-bottom: 10px;
}

.login {
  align-self: center;
  align-content: center;
  display: inline-block;
  background-color: white;
  border-radius: 10px;
  box-shadow: #d4dfe0 0px 0px 5px;
}

.login_content {
  border: 1px solid #d4dfe0;
  border-radius: 10px;
  padding: 5px 20px 20px 20px;
}
</style>
