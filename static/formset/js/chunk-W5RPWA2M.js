var a=class extends Map{constructor(e){super();let t=e.querySelector('meta[name="error-messages"]');if(!t)throw new Error(`${e} requires one <meta name="error-messages"> tag.`);for(let r of t.getAttributeNames()){let s=r.replace(/([_][a-z])/g,o=>o.toUpperCase().replace("_","")),n=t.getAttribute(r);n&&this.set(s,n)}}},i=class{constructor(e){let t=e.closest('[role="group"]'),r=e.form,s=e.closest("django-formset");if(!t||!r||!s)throw new Error(`Attempt to initialize ${e} outside <django-formset>`);let n=r.getAttribute("name")??"__default__";this.fieldGroup=t,this.errorMessages=new a(t),this.endpoint=s.getAttribute("endpoint"),this.fieldName=`${n}.${e.getAttribute("name")}`,r.addEventListener("reset",o=>this.formResetted(o)),r.addEventListener("submitted",o=>this.formSubmitted(o))}};export{a,i as b};
