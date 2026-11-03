# Project Directory Structure

```text
Novex/
├── check_db_data.py
├── check_tables.py
├── COMPLETE_FIX_GUIDE.md
├── create_admin.bat
├── debug_assignment.py
├── FINAL_SOLUTION.md
├── otherllm.md
├── package.json
├── PROFILE_FIX_SUMMARY.md
├── README.md
├── REAL_TIME_LOCATION_IMPLEMENTED.md
├── setup.bat
├── start.bat
├── TEST_PROFILE_FETCH.md
├── assets/
│   ├── LANDDEED2.jpg
│   └── leaf image.webp
├── backend/
│   ├── build.sh
│   ├── create_admin.py
│   ├── gunicorn.conf.py
│   ├── insert_admin_user.sql
│   ├── main.py
│   ├── Procfile
│   ├── PROD_GUIDE.md
│   ├── requirements.txt
│   ├── runtime.txt
│   ├── run_tests.bat
│   ├── start.sh
│   ├── start_server.bat
│   ├── test_all_features.py
│   ├── test_env.py
│   ├── test_extensions.py
│   ├── test_gemini.py
│   ├── test_gemini_v2.py
│   ├── test_import.py
│   ├── test_login_script.py
│   ├── TEST_README.md
│   ├── TEST_RESULTS.md
│   ├── test_results.txt
│   ├── test_results_2.txt
│   ├── test_results_3.txt
│   ├── test_results_final.txt
│   ├── admin/
│   │   └── router.py
│   ├── auth/
│   │   ├── auth_schema.sql
│   │   ├── cloud_storage.py
│   │   ├── email_service.py
│   │   ├── models.py
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── router.py
│   │   ├── session_manager.py
│   │   ├── setup_db.py
│   │   ├── STATUS.md
│   │   ├── SYSTEM_STATUS.md
│   │   └── __init__.py
│   ├── core/
│   │   ├── encryption.key
│   │   ├── supabase_client.py
│   │   └── __init__.py
│   ├── database/
│   │   ├── admin_schema.sql
│   │   ├── agronomists_schema.sql
│   │   ├── CLAIM_APPLICATIONS_ADMIN_MAPPING.md
│   │   ├── claim_applications_schema.sql
│   │   ├── farmer_profiles_complete_schema.sql
│   │   ├── FARMER_PROFILES_MAPPING.md
│   │   ├── farmer_profiles_schema.sql
│   │   ├── field_officers.sql
│   │   ├── fix_assignments_fk.sql
│   │   ├── full_schema.sql
│   │   ├── migrations_autonomous.sql
│   │   ├── migrations_inspections.sql
│   │   ├── migrations_ndvi.sql
│   │   ├── scheme_applications_schema.sql
│   │   ├── supabase_schema.sql
│   │   ├── update_farmer_profiles_for_claims.sql
│   │   └── __init__.py
│   ├── face_auth/
│   │   ├── router.py
│   │   └── __init__.py
│   ├── feature1/
│   │   ├── blockchain_client.py
│   │   ├── blockchain_config.json
│   │   ├── deploy.py
│   │   ├── read_contract.py
│   │   ├── router.py
│   │   ├── services.py
│   │   ├── contracts/
│   │   │   └── LandRegistry.sol
│   ├── feature2/
│   │   ├── agents.py
│   │   ├── agronomist_chat.py
│   │   ├── agronomist_service.py
│   │   ├── claims_service.py
│   │   ├── compensation_agent.py
│   │   ├── decision_intelligence.py
│   │   ├── ensemble_model.tflite
│   │   ├── model_service.py
│   │   ├── pdf_service.py
│   │   ├── predictive_engine.py
│   │   ├── router.py
│   │   ├── satellite_service.py
│   │   └── scheme_application_service.py
│   ├── feature3/
│   │   ├── api.py
│   │   ├── blockchain_logger.py
│   │   ├── database.py
│   │   ├── data_simulator.py
│   │   ├── decision_engine.py
│   │   ├── soil_data.json
│   │   └── twilio_manager.py
│   ├── feature4/
│   │   ├── agent.py
│   │   ├── router.py
│   │   ├── tools.py
│   │   ├── verify_application_storage.py
│   │   └── __init__.py
│   ├── feature4_drl/
│   │   ├── crop_yield_recom.ipynb
│   │   ├── debug_init.py
│   │   ├── enhanced_agriculture_dataset.csv
│   │   ├── pipeline.py
│   │   ├── router.py
│   │   ├── test.py
│   │   ├── __init__.py
│   │   ├── crop_recommendation_models/
│   │   │   ├── model_metadata.json
│   │   │   ├── system_metadata.json
│   │   ├── visualizations/
│   │   │   ├── distributions.png
│   │   │   └── model_performance_evaluation.png
│   ├── feature5/
│   │   ├── equipment_analyzer.py
│   │   ├── router.py
│   │   ├── subsidy_service.py
│   │   └── __init__.py
│   ├── feature6_blockchain/
│   │   ├── blockchain_service.py
│   │   ├── db_schema.sql
│   │   ├── final_schema.sql
│   │   ├── improved_inventory.sql
│   │   ├── qr.png
│   │   ├── router.py
│   │   └── trust_engine.py
│   ├── feature7/
│   │   ├── router.py
│   │   ├── supabase_schema.sql
│   │   └── __init__.py
│   ├── feature_news/
│   │   └── router.py
│   ├── hardware/
│   │   ├── arduino_control.py
│   │   ├── router.py
│   │   ├── __init__.py
│   │   ├── arduino/
│   │   │   ├── arduino_pump_serial.ino
│   │   │   ├── firegas.ino
│   │   │   ├── npwtnano.ino
│   │   │   ├── npwt_sensor.ino
│   │   │   ├── npwt_sensor_wifi.ino
│   │   │   └── pump_control.ino
│   ├── inspections/
│   │   ├── models.py
│   │   ├── pdf_service.py
│   │   ├── router.py
│   │   └── __init__.py
│   ├── mandi/
│   │   └── router.py
│   ├── scripts/
│   │   ├── check_imports.py
│   │   ├── check_models.py
│   │   ├── convert_dataset.py
│   │   ├── create_default_users.py
│   │   ├── data_augmentation.py
│   │   ├── debug_db.py
│   │   ├── debug_models.py
│   │   ├── gen_pass.py
│   │   ├── import_result.txt
│   │   ├── seed_inspections_data.py
│   │   ├── test_agent.py
│   │   ├── test_output.txt
│   │   ├── test_pipeline.py
│   │   ├── test_result.txt
│   │   └── __init__.py
│   ├── services/
│   │   ├── mandi_service.py
│   │   ├── sensor_service.py
│   │   ├── sms_service.py
│   │   └── __init__.py
├── docs/
│   ├── ADMIN_ACCESS_GUIDE.md
│   ├── ADMIN_REDIRECT_FIX.md
│   ├── DASHBOARD_FIRE_GAS_AGRONOMIST_FIX.md
│   ├── FEATURE3_RECOMMENDATIONS_COMPLETE.md
│   ├── FEATURE7_DYNAMIC_IMPLEMENTATION.md
│   ├── FINAL_STATUS.md
│   ├── FINAL_TEST_RESULTS.md
│   ├── FIRE_GAS_MONITORING_UPDATE.md
│   ├── FIRE_GAS_SENSOR_FIX.md
│   ├── PROTECTION_DISABLED.md
│   └── SENSOR_INTEGRATION_COMPLETE.md
├── document_md/
│   ├── ADMIN_CLAIMS_GUIDE.md
│   ├── ADMIN_DASHBOARD_GUIDE.md
│   ├── BROADCAST_GUIDE.md
│   ├── BUG_FIX_REPORT.md
│   ├── CLAIMS_SYSTEM_COMPLETE.md
│   ├── DEPLOYMENT.md
│   ├── DEPLOYMENT_FIXED.md
│   ├── DEPLOYMENT_GUIDE.md
│   ├── DEPLOY_NOW.md
│   ├── DEPLOY_QUICK.md
│   ├── DOCS_VIEW_GUIDE.md
│   ├── EARTH_UPDATE_LOG.md
│   ├── FACE_AUTH_IMPLEMENTATION.md
│   ├── FACE_SIGNUP_README.md
│   ├── FIXES_APPLIED.md
│   ├── INLINE_PREVIEW_GUIDE.md
│   ├── MOTOR_TROUBLESHOOTING.md
│   ├── NAVBAR_UPDATE.md
│   ├── NDVI_CLAIM_FEATURE.md
│   ├── NDVI_CONFIG.md
│   ├── NDVI_FIX_SUMMARY.md
│   ├── PDF_CERTIFICATE_GUIDE.md
│   ├── PERSISTENCE_FIX.md
│   ├── PRESENTATION_SCRIPT.md
│   ├── PROFILE_FIX_SUMMARY.md
│   ├── README.md
│   ├── RENDER_ENV_SETUP.md
│   ├── RENDER_MEMORY_FIX.md
│   ├── SATELLITE_CLAIMS_MANUAL.md
│   ├── UI_REFINEMENT_LOG.md
│   └── VERCEL_DEPLOYMENT_GUIDE.md
├── frontend/
│   ├── ALL_ROUTES.txt
│   ├── build_err.log
│   ├── build_err_utf8.log
│   ├── COLOR_GUIDE.md
│   ├── COMPLETE_IMPLEMENTATION.md
│   ├── COMPONENT_SHOWCASE.md
│   ├── ENHANCED_FEATURES_GUIDE.md
│   ├── eslint.config.js
│   ├── FINAL_IMPLEMENTATION.md
│   ├── FINAL_ROUTES_AND_FIXES.md
│   ├── FINAL_SUMMARY.md
│   ├── fix_theme.py
│   ├── IMAGES_AND_ROUTES.md
│   ├── IMPLEMENTATION_COMPLETE.md
│   ├── index.html
│   ├── MAIN_ROUTE.txt
│   ├── MODERNIZATION_SUMMARY.md
│   ├── MODERN_UI_README.md
│   ├── package.json
│   ├── postcss.config.js
│   ├── QUICK_REFERENCE.md
│   ├── QUICK_START.md
│   ├── README.md
│   ├── README_MODERN_UI.md
│   ├── server.js
│   ├── SETUP_GUIDE.md
│   ├── tailwind.config.js
│   ├── vercel.json
│   ├── vite.config.js
│   ├── public/
│   │   ├── browserconfig.xml
│   │   ├── clear-cache.html
│   │   ├── grid-pattern.svg
│   │   ├── logo.png
│   │   ├── manifest.json
│   │   ├── pwa-192x192.svg
│   │   ├── pwa-512x512.svg
│   │   ├── qr_code.png
│   │   ├── vite.svg
│   │   ├── assets/
│   │   │   ├── farmer-crop-scan.jpg.png
│   │   │   ├── field-crop.jpg
│   │   │   ├── iot-testing.png
│   │   │   ├── land.jpg
│   │   │   ├── leaf-image.webp
│   │   │   ├── Market.png
│   │   │   └── smart_irrigation.png
│   │   ├── locales/
│   │   │   ├── en/
│   │   │   │   └── translation.json
│   │   │   ├── hi/
│   │   │   │   └── translation.json
│   │   │   ├── mr/
│   │   │   │   └── translation.json
│   │   ├── models/
│   │   │   ├── age_gender_model-shard1
│   │   │   ├── age_gender_model-weights_manifest.json
│   │   │   ├── face_expression_model-shard1
│   │   │   ├── face_expression_model-weights_manifest.json
│   │   │   ├── face_landmark_68_model-shard1
│   │   │   ├── face_landmark_68_model-weights_manifest.json
│   │   │   ├── face_landmark_68_tiny_model-shard1
│   │   │   ├── face_landmark_68_tiny_model-weights_manifest.json
│   │   │   ├── face_recognition_model-shard1
│   │   │   ├── face_recognition_model-shard2
│   │   │   ├── face_recognition_model-weights_manifest.json
│   │   │   ├── mtcnn_model-shard1
│   │   │   ├── mtcnn_model-weights_manifest.json
│   │   │   ├── ssd_mobilenetv1_model-shard1
│   │   │   ├── ssd_mobilenetv1_model-shard2
│   │   │   ├── ssd_mobilenetv1_model-weights_manifest.json
│   │   │   ├── tiny_face_detector_model-shard1
│   │   │   └── tiny_face_detector_model-weights_manifest.json
│   ├── src/
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── BetterCart_CopyThis.jsx
│   │   ├── i18n.js
│   │   ├── index.css
│   │   ├── main.jsx
│   │   ├── supabaseClient.js
│   │   ├── admin/
│   │   │   ├── components/
│   │   │   │   ├── SpotlightCard.css
│   │   │   │   └── SpotlightCard.jsx
│   │   │   ├── layout/
│   │   │   │   ├── AdminLayout.jsx
│   │   │   │   └── AdminSidebar.jsx
│   │   │   ├── pages/
│   │   │   │   ├── AdminDashboard.jsx
│   │   │   │   ├── AdminReports.jsx
│   │   │   │   ├── AdminSchemes.jsx
│   │   │   │   ├── Broadcast.jsx
│   │   │   │   ├── ClaimDetail.jsx
│   │   │   │   ├── ClaimListing.jsx
│   │   │   │   ├── Claims.jsx
│   │   │   │   └── FieldAssignments.jsx
│   │   ├── api/
│   │   │   └── faceAuthClient.js
│   │   ├── assets/
│   │   │   ├── logo.png
│   │   │   ├── react.svg
│   │   │   ├── images/
│   │   │   │   ├── auth-face.svg
│   │   │   │   └── auth-idle.svg
│   │   ├── components/
│   │   │   ├── ErrorBoundary.jsx
│   │   │   ├── ProtectedRoute.jsx
│   │   │   ├── CropHealth/
│   │   │   │   ├── CameraDiagnose.jsx
│   │   │   │   ├── Dashboard.jsx
│   │   │   │   ├── DecisionIntelligence.jsx
│   │   │   │   ├── InsuranceForm.jsx
│   │   │   │   ├── NDVITimeSeries.jsx
│   │   │   │   ├── PredictiveAlerts.jsx
│   │   │   │   ├── SatelliteMonitor.jsx
│   │   │   │   └── ZoneAnalysis.jsx
│   │   │   ├── Dashboard/
│   │   │   │   └── EconomicImpact.jsx
│   │   │   ├── Feature3/
│   │   │   │   ├── FarmDashboard.jsx
│   │   │   │   ├── Recommendations.jsx
│   │   │   │   └── TrustReport.jsx
│   │   │   ├── Feature4/
│   │   │   │   ├── AskAI.jsx
│   │   │   │   ├── BrowseSchemes.jsx
│   │   │   │   ├── CompleteFarmerProfile.jsx
│   │   │   │   ├── FarmerProfile.jsx
│   │   │   │   ├── MyApplications.jsx
│   │   │   │   └── SchemeCard.jsx
│   │   │   ├── Feature6/
│   │   │   │   ├── BlockchainManager.jsx
│   │   │   │   └── InventoryManager.jsx
│   │   │   ├── features/
│   │   │   │   ├── AIExplanationCard.jsx
│   │   │   │   ├── CameraCapture.jsx
│   │   │   │   ├── CropHealth.jsx
│   │   │   │   ├── DynamicFeatureSection.jsx
│   │   │   │   ├── EquipmentHealthCard.jsx
│   │   │   │   ├── FertilizationAI.jsx
│   │   │   │   ├── FireDetectionCard.jsx
│   │   │   │   ├── FireGasMonitor.jsx
│   │   │   │   ├── GasMonitoringCard.jsx
│   │   │   │   ├── ImageUploader.jsx
│   │   │   │   ├── MaintenanceChart.jsx
│   │   │   │   ├── MaintenanceScheduleCard.jsx
│   │   │   │   ├── MandiPrices.jsx
│   │   │   │   ├── ModuleSelection.jsx
│   │   │   │   ├── NearbyShops.jsx
│   │   │   │   ├── OfflineIndicator.jsx
│   │   │   │   ├── RepairRecommendations.jsx
│   │   │   │   ├── ServicesSection.jsx
│   │   │   │   ├── SmartIrrigation.jsx
│   │   │   │   ├── SoilHealthCards.jsx
│   │   │   │   ├── SubsidyInfo.jsx
│   │   │   │   ├── TodaysActionCard.jsx
│   │   │   │   ├── WeatherForecast.jsx
│   │   │   │   ├── ZoneMap.jsx
│   │   │   │   ├── CropRecommendation/
│   │   │   │   │   └── CropRecommendation.jsx
│   │   │   │   ├── DisasterNews/
│   │   │   │   │   └── DisasterNews.jsx
│   │   │   ├── layout/
│   │   │   │   ├── CustomCursor.jsx
│   │   │   │   ├── GlobalBackground.jsx
│   │   │   │   ├── GooeyNavbar.jsx
│   │   │   │   ├── LanguageSwitcher.jsx
│   │   │   │   ├── PageIntroHandler.jsx
│   │   │   │   └── VoiceFloatingButton.jsx
│   │   │   ├── MarkMyLand/
│   │   │   │   ├── DocumentUpload.jsx
│   │   │   │   ├── LandMap.jsx
│   │   │   │   └── MarkMyLand.jsx
│   │   │   ├── pwa/
│   │   │   │   └── ReloadPrompt.jsx
│   │   │   ├── react-bits/
│   │   │   │   └── SpotlightCard.jsx
│   │   │   ├── three/
│   │   │   │   ├── CursorWaves.jsx
│   │   │   │   ├── Earth3D.jsx
│   │   │   │   ├── EarthWaves.jsx
│   │   │   │   └── GalaxyBackground.jsx
│   │   │   ├── ui/
│   │   │   │   ├── AuroraBackground.jsx
│   │   │   │   ├── CardSwap.jsx
│   │   │   │   ├── GlassCard.jsx
│   │   │   │   ├── ModernNavbar.jsx
│   │   │   │   └── StatCard.jsx
│   │   ├── config/
│   │   │   └── api.js
│   │   ├── constants/
│   │   │   ├── languages.js
│   │   │   └── pageIntros.js
│   │   ├── hooks/
│   │   │   └── usePageIntro.js
│   │   ├── pages/
│   │   │   ├── AddBatch.jsx
│   │   │   ├── AuthPage.jsx
│   │   │   ├── ClaimApplication.jsx
│   │   │   ├── CropHealthModern.jsx
│   │   │   ├── DebugAuth.jsx
│   │   │   ├── EnhancedLandingPage.jsx
│   │   │   ├── EquipmentAnalyzer.jsx
│   │   │   ├── FaceAuth.jsx
│   │   │   ├── FarmerDashboard.jsx
│   │   │   ├── FarmerInventory.jsx
│   │   │   ├── FarmerProfile.jsx
│   │   │   ├── FeaturesPage.jsx
│   │   │   ├── InspectorDashboard.jsx
│   │   │   ├── LandingPage.jsx
│   │   │   ├── Marketplace.jsx
│   │   │   ├── ModernFarmerDashboard.jsx
│   │   │   ├── ModernFeatures.jsx
│   │   │   ├── ModernInventory.jsx
│   │   │   ├── ModernLandingPage.jsx
│   │   │   ├── ModernMarketplace.jsx
│   │   │   ├── ModernProfile.jsx
│   │   │   ├── ProductTransparency.jsx
│   │   │   ├── SchemesAgent.jsx
│   │   │   └── SchemesPage.jsx
│   │   ├── services/
│   │   │   ├── llmService.js
│   │   │   ├── marketService.js
│   │   │   └── newsService.js
│   │   ├── store/
│   │   │   ├── equipmentStore.js
│   │   │   └── themeStore.js
│   │   ├── utils/
│   │   │   ├── cn.js
│   │   │   ├── localVoiceProcessor.js
│   │   │   └── routeConfig.js
├── logs/
│   ├── error_log.txt
│   └── zzzzz.txt
├── notebooks/
│   ├── crop_data_generator.py
│   ├── crop_disease.ipynb
│   ├── crop_yield_recommendation.ipynb
│   ├── crop_yield_recommendation_updated.ipynb
│   ├── hybrid_agri_dataset_2000rows.csv
│   ├── jaishreeram.ipynb
│   ├── meta_cells_output.txt
│   ├── neelay_joshi_4am_crop_recommendation.ipynb
│   ├── catboost_info/
│   │   ├── catboost_training.json
│   │   ├── learn_error.tsv
│   │   ├── test_error.tsv
│   │   ├── time_left.tsv
│   │   ├── learn/
│   │   │   └── events.out.tfevents
│   │   ├── test/
│   │   │   └── events.out.tfevents
│   ├── models/
│   │   ├── tft_model.pth
│   ├── models_prod/
│   │   ├── catboost_prod.cbm
│   │   ├── diagnostics.png
│   ├── models_v2/
│   │   ├── catboost_p10.cbm
│   │   ├── catboost_p50.cbm
│   │   ├── catboost_p90.cbm
│   │   ├── feature_importance.csv
│   │   └── production_results.png
│   ├── visualizations/
│   │   ├── 1_actual_vs_predicted.png
│   │   ├── 2_residual_plots.png
│   │   ├── 3_error_distribution.png
│   │   ├── 4_model_comparison.png
│   │   ├── 5_feature_importance.png
│   │   ├── 6_error_boxplot.png
│   │   ├── 7_error_heatmap.png
│   │   └── 8_metrics_table.png
```
